from rest_framework.serializers import ModelSerializer
from .models import JabamaUser
from django.contrib.auth.hashers import make_password


class JabamaUsersSerializer(ModelSerializer):
    class Meta:
        model = JabamaUser
        fields = "__all__"
    
    
    def validate(self, attrs):
        password = attrs.get('password', None)
        if password:
            attrs['password'] = make_password(password)
        return super().validate(attrs)
        