from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Persona, Vehiculo, Oficial, Infraccion

# Register your models here.
admin.site.register(Persona)
admin.site.register(Vehiculo)
admin.site.register(Oficial)
admin.site.register(Infraccion)
