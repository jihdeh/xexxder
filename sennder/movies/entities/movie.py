from typing import List

from sennder.movies.entities.person import PersonEntity


class MovieEntity:
    """Movie Entity

    Single movie entity data structure
    """

    id = str
    title = str
    description = str
    release_date = int

    def __setitem__(self, key, value):
        self.key = value


class MappedMovieEntity(MovieEntity):
    """Mapped Movie Entity

    List of movies entity data structure
    """

    people = List[PersonEntity]
