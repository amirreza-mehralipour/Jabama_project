from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from django import filters

class ListCreatePlace(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['capacity']  
    search_fields = ['addres', 'owner__username'] 
    ordering_fields = ['capacity'] 

    def get_queryset(self):
        return Place.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyPlace(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(owner = self.request.user)
    
    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this place.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this place.")
        instance.delete()


class ListCreateAdvertisement(ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    peremission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Advertisement.objects.filter(place__owner=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['place'].owner != self.request.user:
            raise PermissionDenied("You do not have permission to create an advertisement for this place.")
        serializer.save()


class RetrieveUpdateDestroyAdvertisement(RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Advertisement.objects.filter(place__owner=self.request.user)

    def perform_update(self, serializer):
        if self.get_object().place.owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this advertisement.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.place.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this advertisement.")
        instance.delete()
