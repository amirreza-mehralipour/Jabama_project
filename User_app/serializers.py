from rest_framework.serializers import ModelSerializer
from .models import JabamaUser


class JabamaUserSerializer(ModelSerializer):
    class Meta:
        model = JabamaUser
        fields = "__all__"