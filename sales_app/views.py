from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


class ListCreateSale(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sales.objects.filter(customer = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(customer = self.request.user)


class RetrieveUpdateDestroySales(RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sales.objects.filter(customer=self.request.user)

    def perform_update(self, serializer):
        if self.get_object().customer != self.request.user:
            raise ValidationError("You do not have permission to update this sale.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.customer != self.request.user:
            raise ValidationError("You do not have permission to delete this sale.")
        instance.delete()

