from django.db import models
from django.contrib.auth.models import AbstractUser


class JabamaUser(AbstractUser):
    rule_choices = [
        ('S', 'Seller'),
        ('B', 'Buyer'),
    ]


    jabama_rule = models.CharField(max_length= 1, choices= rule_choices)

    def __str__(self) -> str:
        return self.username