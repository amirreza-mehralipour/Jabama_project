from django.db import models
from django.contrib.auth.models import User


class JabamaUsers(User, models.Model):
    rule_choices = [
        ('S', 'Seller'),
        ('B', 'Buyer'),
    ]


    jabama_rule = models.CharField(max_length= 1, choices= rule_choices)