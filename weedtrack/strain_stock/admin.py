from django.contrib import admin
from .models import StrainStock, StrainOperation

# Register your models here.

admin.site.register(StrainStock)
admin.site.register(StrainOperation)
