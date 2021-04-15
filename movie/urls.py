from django.urls import path

from .views import *

urlpatterns = [
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('collection/', MovieCollectionListCreateView.as_view(), name='movie-collection'),
    path('collection/<str:uuid>', MovieCollectionRetrieveUpdateDeleteView.as_view(),
         name='movie-collection_read_update_delete'),
]
