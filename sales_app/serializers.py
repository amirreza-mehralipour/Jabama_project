from rest_framework.serializers import ModelSerializer
from .models import *


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'