from django.db import models
from django.contrib.auth.models import User


class JabamaUser(User):
    is_buyer = models.BooleanField(default= False)
