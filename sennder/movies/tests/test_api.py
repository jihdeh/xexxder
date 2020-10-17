# type: ignore
import requests_mock
import unittest
from django.test import RequestFactory
from unittest.mock import patch

from sennder.movies.services.api import MovieService
from sennder.movies.views import MoviesView
from sennder.movies.tests.mock_data import (
    test_movie_url,
    test_people_url,
    test_people_resp,
    test_movies_resp,
    test_movie_url_second,
)

data = {"movies": []}
expire = 60


class TestMappingLogic(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.movies = test_movies_resp

    def set(self, key, val):
        data[key] = val

    def get(self, key):
        return data[key]

    def expire(self, key, value):
        return expire

    MOCK_PEOPLE_ADDRESS = test_people_url
    MOCK_MOVIE_ADDRESS_ONE = test_movie_url
    MOCK_MOVIE_ADDRESS_TWO = test_movie_url_second

    @requests_mock.Mocker()
    @patch("redis.StrictRedis.set")
    @patch("redis.StrictRedis.get")
    @patch("redis.StrictRedis.expire")
    def test_movies_response(
        self,
        mock_request,
        mock_redis_set,
        mock_redis_get,
        mock_redis_expire,
    ):
        mock_redis_set.side_effect = self.set
        mock_redis_get.side_effect = self.get
        mock_redis_expire.side_effect = self.expire

        mock_request.get(self.MOCK_PEOPLE_ADDRESS, json=test_people_resp)
        mock_request.get(self.MOCK_MOVIE_ADDRESS_ONE, json=test_movies_resp[0])
        mock_request.get(self.MOCK_MOVIE_ADDRESS_TWO, json=test_movies_resp[1])
        service = MovieService()
        service_request = service.get()

        # Views Test MoviesView() as if it were deployed at /movies
        request = self.factory.get("/movies")
        view = MoviesView()
        response = view.get_context_data(request)

        self.assertListEqual(response["movies"], test_movies_resp)
        self.assertListEqual(service_request, test_movies_resp)

    @requests_mock.Mocker()
    @patch("redis.StrictRedis.set")
    @patch("redis.StrictRedis.get")
    @patch("redis.StrictRedis.expire")
    def test_movies_response_no_result(
        self, mock_request, mock_redis_set, mock_redis_get, mock_redis_expire
    ):
        mock_redis_set.side_effect = self.set
        mock_redis_get.side_effect = self.get

        service = MovieService()

        mock_request.get(
            self.MOCK_PEOPLE_ADDRESS, json=test_people_resp, status_code=400
        )

        request = service.get()

        self.assertEqual(request, [])
