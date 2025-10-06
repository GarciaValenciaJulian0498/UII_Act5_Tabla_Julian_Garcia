from django.contrib import admin

# Register your models here.
from .models import Profesor

# Registrar profesor 
admin.site.register(Profesor)