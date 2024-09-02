from django.contrib.admin import register, ModelAdmin
from .models import JabamaUser


@register(JabamaUser)
class JabamaUsersAdmin(ModelAdmin):
    pass