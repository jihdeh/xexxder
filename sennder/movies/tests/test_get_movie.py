# type: ignore
import requests_mock
import unittest

from sennder.movies.services.api import MovieService
from sennder.movies.tests.mock_data import (
    test_movie_url,
    test_movie_resp,
)


class TestGetMovie(unittest.TestCase):
    MOCK_ADDRESS = test_movie_url

    @requests_mock.Mocker()
    def test_movie(self, m):
        service = MovieService()
        m.get(self.MOCK_ADDRESS, json=test_movie_resp)
        req = service.get_movies(test_movie_url)

        self.assertEqual(len(req), len(test_movie_resp))
        self.assertEqual(req["title"], "Castle in the Sky")

    @requests_mock.Mocker()
    def test_movie_bad_request(self, m):
        service = MovieService()
        m.get(self.MOCK_ADDRESS, json=test_movie_resp, status_code=400)
        req = service.get_movies(test_movie_url)
        self.assertEqual(req, {})
