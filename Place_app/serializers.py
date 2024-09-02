from rest_framework.serializers import ModelSerializer
from .models import *


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


