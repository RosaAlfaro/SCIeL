from django.contrib import admin
from .models import *

admin.site.register(Cultivo)

admin.site.register(Invernadero)

admin.site.register(Etapa)

admin.site.register(Dispositivo)

admin.site.register(Sensor)

admin.site.register(Actuador)

admin.site.register(Medicion)

admin.site.register(Parametro)
