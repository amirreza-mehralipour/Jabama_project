from django.urls import path
from .views import *


urlpatterns = [
    path('place/', ListCreatePlace.as_view()),
    path('place/change/<int:pk>/', RetrieveUpdateDestroyPlace.as_view()),
    path('ad/', ListCreateAdvertisement.as_view()),
    path('ad/change/<int:pk>/', RetrieveUpdateDestroyAdvertisement.as_view()),
]