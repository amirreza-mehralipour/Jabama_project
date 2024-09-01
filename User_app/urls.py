from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('refresh/', Refresh.as_view()),
    path('user/', ListCreateUser.as_view()),
    path('user/change/<int:pk>/', RetrieveUpdateDestroyUser.as_view())
]