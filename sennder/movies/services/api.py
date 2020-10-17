from typing import List, Union

from django.conf import settings  # type: ignore
import requests  # type: ignore

from sennder.movies.services.cache import RedisCache
from sennder.movies.entities.movie import MovieEntity, MappedMovieEntity
from sennder.movies.entities.person import PersonEntity


redis = RedisCache()


class MovieService:

    BASE_URL = settings.MOVIE_BASE_API_URL
    REDIS_MOVIES_KEY = "movies"

    def get_people(self) -> List[PersonEntity]:
        """Get all people

        Request to get all people
        """
        url = "{}/people".format(self.BASE_URL)
        params = {"fields": "id,name,films", "limit": 250}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            # OP: use proper logger here, throw error and catch in caller
            return []
        return response.json()

    def get_movies(self, movie_url: str) -> Union[MovieEntity, dict]:
        """Return a movie data

        Makes external request to fetch movie data
        """

        params = {"fields": "id,title,description,release_date"}
        response = requests.get(movie_url, params=params)
        if response.status_code != 200:
            # OP: use proper logger here, throw error and catch in caller
            return {}
        return response.json()

    def get(self) -> List[MappedMovieEntity]:
        """Return a list of movies

        Method returns a filtered list of movies with their actors
        And saving to cache
        """

        redis_movie_value = redis.get(self.REDIS_MOVIES_KEY)
        if redis_movie_value:
            return redis_movie_value
        people = self.get_people() or []
        print(len(people))  # remove this later

        return self.map_person_to_movies(people)

    def map_person_to_movies(
        self,
        people: List[PersonEntity],
    ) -> List[MappedMovieEntity]:
        """Perform mapping logic

        Method to map persons to movies
        """

        movie_urls_hash_store = {}
        structured_movie_data = []

        for person in people:
            movies = person["films"]
            for movie_url in movies:
                if movie_url in movie_urls_hash_store:
                    # skip adding to hash
                    # but add person to movie list via index
                    movie_url_index_value = movie_urls_hash_store[movie_url]
                    movie = structured_movie_data[movie_url_index_value]

                    # if person[films] has movie id then add
                    person_movie_id = movie_url.split("/")[-1]
                    if person_movie_id == movie["id"]:
                        movie["people"].append(person)
                        structured_movie_data[movie_url_index_value] = movie
                else:
                    # then add new movie w/ person to list
                    get_movie_data = self.get_movies(movie_url)
                    if get_movie_data:
                        movie = get_movie_data
                        movie["people"] = [person]
                        structured_movie_data.append(movie)
                        movie_urls_hash_store[movie_url] = (
                            len(structured_movie_data) - 1
                        )

        movie_urls_hash_store = {}

        redis.set(self.REDIS_MOVIES_KEY, structured_movie_data)
        return structured_movie_data
        # - Optimal space & time complexity
        # O(n) time | O(n) space - where n is the length of the input array
