from django.shortcuts import render
from .serializers import JabamaUsersSerializer
from .models import JabamaUsers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass 


class ListCreateUser(ListCreateAPIView):
    queryset = JabamaUsers.objects.all()
    serializer_class = JabamaUsersSerializer


class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    queryset = JabamaUsers
    serializer_class = JabamaUsersSerializer
