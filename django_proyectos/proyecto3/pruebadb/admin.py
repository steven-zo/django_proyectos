from django.contrib import admin
from .models import Empresa, Programador
# Register your models here.
# se debe registrar la tabla o el modelo recientemente creado desde models.py
admin.site.register(Empresa)
admin.site.register(Programador)