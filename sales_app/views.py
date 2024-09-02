from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


class ListCreateSale(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroySales(RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

