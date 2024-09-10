from django.contrib.admin import register, ModelAdmin
from .models import *

@register(Sales)
class SalesAdmin(ModelAdmin):
    pass


@register(Rating)
class RatingAdmin(ModelAdmin):
    pass

