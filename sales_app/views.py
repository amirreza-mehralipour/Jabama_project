from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


class ListCreatePlace(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer


class RetrieveUpdateDestroySales(RetrieveUpdateDestroyAPIView)
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer

    