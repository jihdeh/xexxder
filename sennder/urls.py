from django.contrib import admin
from django.urls import path

from sennder.movies.views import MoviesView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "movies/",
        MoviesView.as_view(template_name="movies/movies.html"),
        name="Movies View",
    ),
]
