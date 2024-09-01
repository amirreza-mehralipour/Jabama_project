from django.contrib.admin import register, ModelAdmin
from .models import JabamaUsers


@register(JabamaUsers)
class JabamaUsersAdmin(ModelAdmin):
    pass