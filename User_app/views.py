from django.shortcuts import render
from .serializers import JabamaUserSerializer
from .models import JabamaUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import ListCreateAPIView


class CreateAndShowUser(ListCreateAPIView):
    queryset = JabamaUser.objects.all()
    serializer_class = JabamaUserSerializer


    def perform_create(self, serializer):
        password = self.request.data.get('password')
        user = serializer.save()
        if password:
            user.set_password(password)
            user.save()


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass 


