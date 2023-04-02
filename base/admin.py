from django.contrib import admin

# Register your models here.
from .models import Place,Messages
admin.site.register(Place)
admin.site.register(Messages)