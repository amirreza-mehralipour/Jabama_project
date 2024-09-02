from typing import Iterable
from django.db import models
from User_app.models import JabamaUsers
from Place_app.models import Place, Advertisement
from django.core.exceptions import ValidationError

class Sales(models.Model):
    customer = models.ForeignKey(JabamaUsers, on_delete= models.PROTECT)
    advertisement = models.OneToOneField(Advertisement, on_delete= models.PROTECT)

    def clean(self):
        super().clean()
        if self.customer.jabama_rule != 'B':
            raise ValidationError('customer must be a buyer user')
        

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'Sales'
