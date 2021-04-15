from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .redis import redis_instance
from user.services import UserService
user_service = UserService()


class UserRegisterView(APIView):
    '''user registration- email and password'''
    permission_classes = [AllowAny]

    def post(self, request):
        return user_service.register(data=request.data)


class UserLoginView(APIView):
    '''user login- email and password'''
    permission_classes = [AllowAny]

    def post(self, request):
        return user_service.login(data=request.data)


class RequestCountView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        count = 0
        count = redis_instance.get('counter')
        return Response(data={'requests': int(count)})


class RequestCountResetView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        count = redis_instance.set('counter', 0)
        return Response(data={'message': 'request counter reset successfully'})
