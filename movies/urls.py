# app/movies/urls.py

from django.urls import include, path
from rest_framework import routers

from .views import MoviesViewSet

# from .views import MovieList, MovieDetail

router = routers.SimpleRouter()
router.register(r"movies", MoviesViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    # path("api/movies/", MovieList.as_view()),
    # path("api/movies/<int:pk>/", MovieDetail.as_view()),
]
