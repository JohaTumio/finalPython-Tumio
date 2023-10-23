from django.contrib import admin
from .models import Animal, Cuidador, Profesional, Adopcion

admin.site.register(Animal)
admin.site.register(Cuidador)
admin.site.register(Profesional)
admin.site.register(Adopcion)
