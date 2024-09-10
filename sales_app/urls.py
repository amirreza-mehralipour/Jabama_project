from django.urls import path
from .views import *


urlpatterns = [
    path('sales/', ListCreateSale.as_view()),
    path('sales/change/<int:pk>/', RetrieveUpdateDestroySales.as_view()),
    path('rate/', ListCreateRating.as_view()),
]