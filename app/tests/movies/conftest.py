import pytest

from movies.models import Movie


@pytest.fixture(scope="function")
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie

    return _add_movie


@pytest.fixture(scope="function")
def remove_movie():
    def _remove_movie(title, genre, year):
        movie = Movie.objects.delete(title=title, genre=genre, year=year)
        return movie

    return _remove_movie
