from django.views.generic import TemplateView  # type: ignore

from sennder.movies.services.api import MovieService  # type: ignore


class MoviesView(TemplateView):
    template_name = "movies/movies.html"

    def get_context_data(self, *args, **kwargs):
        movie_service = MovieService()
        movies = movie_service.get()
        context = {"movies": movies}
        return context
