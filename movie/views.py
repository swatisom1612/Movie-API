from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.permissions import IsOwnerOrAdmin
from .models import MovieCollection
from .services import MovieService

service = MovieService()


class MovieListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        """this gives movie data from  https://demo.credy.in/api/v1/maya/movies/ """
        page = request.query_params.get('page')
        return service.movie_list(page)


class MovieCollectionListCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        """method for creating new movie collection"""
        return service.create(request=request)

    def get(self, request):
        """method for getting movie collection list"""
        return service.list(request=request)


class MovieCollectionRetrieveUpdateDeleteView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication

    def get_queryset(self):
        return MovieCollection.objects.prefetch_related('collection_movies').get(pk=self.kwargs['uuid'],
                                                                                 is_active=True, is_delete=False)

    def get(self, request, *args, **kwargs):
        """method for get request for  movie collection"""
        try:
            self.check_object_permissions(self.request, self.get_queryset())
            return service.retrieve(instance=self.get_queryset())
        except MovieCollection.DoesNotExist:
            return Response({
                'error': 'Invalid UUID'
            })

    def put(self, request, *args, **kwargs):
        """method for PUT request movie collection"""
        try:
            self.check_object_permissions(self.request, self.get_queryset())
            return service.update(request=request, instance=self.get_queryset())
        except MovieCollection.DoesNotExist:
            return Response({
                'error': 'Invalid UUID'
            })

    def delete(self, request, *args, **kwargs):
        """method for DELETE request movie collection"""
        try:
            self.check_object_permissions(self.request, self.get_queryset())
            return service.delete(instance=self.get_queryset())
        except MovieCollection.DoesNotExist:
            return Response({
                'error': 'Invalid UUID'
            })
