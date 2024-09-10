from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ListCreateSale(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["advertisement__price", "advertisement__start_time"]
    search_fields = [
        "advertisement__place__addres", 
        "advertisement__place__owner__username", 
        "advertisement__price"
    ]

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


class ListCreateRating(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "GET":
            self.permission_classes = [AllowAny]
        return super(ListCreateRating, self).get_permissions()