from django.contrib.admin import register, ModelAdmin
from .models import *

@register(Place, Advertisement)
class PlaceAdmin(ModelAdmin):
    pass


class AdvertisementAdmin(ModelAdmin):
    pass

