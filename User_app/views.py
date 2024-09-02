from django.shortcuts import render
from .serializers import JabamaUsersSerializer
from .models import JabamaUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass 


class ListCreateUser(ListCreateAPIView):
    queryset = JabamaUser.objects.all()
    serializer_class = JabamaUsersSerializer


class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    queryset = JabamaUser
    serializer_class = JabamaUsersSerializer
