from rest_framework.serializers import ModelSerializer
from .models import *


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'