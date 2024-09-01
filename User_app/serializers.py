from rest_framework.serializers import ModelSerializer
from .models import JabamaUsers
from django.contrib.auth.hashers import make_password


class JabamaUsersSerializer(ModelSerializer):
    class Meta:
        model = JabamaUsers
        fields = "__all__"
    
    
    def validate_password(self, value):
        return make_password(value)

    def to_internal_value(self, data):
        if 'password' in data:
            data['password'] = make_password(data['password'])
        return super().to_internal_value(data)