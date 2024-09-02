from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from User_app.models import JabamaUsers

class Place(models.Model):
    owner = models.ForeignKey(JabamaUsers, on_delete= models.CASCADE)
    addres = models.TextField()
    capacity = models. IntegerField()

    def clean(self):
        super().clean()
        if self.owner.jabama_rule != "S":
            return ValidationError("owner must be a seller user",)
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.owner}'s {self.addres} Place"

class Advertisement(models.Model):
    place = models.ForeignKey(Place, on_delete= models.CASCADE)
    price = models.IntegerField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    def clean(self) -> None:
        super().clean()
        if self.finish_time < self.start_time:
            return ValidationError("Finish time cannot be earlier than start time.")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.place.owner}' advertiesment for {self.place} Place for {self.start_time} to {self.finish_time}"