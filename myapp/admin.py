from django.contrib import admin
from .models import Coordenadas, Rotas, Paradas, Onibus
# Register your models here.

admin.site.register(Coordenadas)
admin.site.register(Rotas)
admin.site.register(Paradas)
admin.site.register(Onibus)