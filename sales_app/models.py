from typing import Iterable
from django.db import models
from User_app.models import *
from Place_app.models import Place, Advertisement
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class Sales(models.Model):
    customer = models.ForeignKey(JabamaUser, on_delete= models.PROTECT)
    advertisement = models.OneToOneField(Advertisement, on_delete= models.PROTECT)

    def clean(self):
        super().clean()
        if self.customer.jabama_rule != 'B':
            raise ValidationError('customer must be a buyer user')
        

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.customer.username} deal for {self.advertisement}"

    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'Sales'


class Rating(models.Model):
    user = models.ForeignKey(JabamaUser, on_delete= models.PROTECT)
    sale = models.ForeignKey(Sales, on_delete= models.PROTECT)
    rate = models.IntegerField(validators= [
        MaxValueValidator(1, message='rating must be between 1-5'),
        MaxValueValidator(5, message='rating must be between 1-5')
    ])
    comment = models.TextField()
