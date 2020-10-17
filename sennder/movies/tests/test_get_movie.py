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
    def test_movie(self, mock_request):
        service = MovieService()
        mock_request.get(self.MOCK_ADDRESS, json=test_movie_resp)
        request = service.get_movies(test_movie_url)

        self.assertEqual(len(request), len(test_movie_resp))
        self.assertEqual(request["title"], "Castle in the Sky")

    @requests_mock.Mocker()
    def test_movie_bad_request(self, mock_request):
        service = MovieService()
        mock_request.get(
            self.MOCK_ADDRESS, json=test_movie_resp, status_code=400
        )
        request = service.get_movies(test_movie_url)
        self.assertEqual(request, {})
