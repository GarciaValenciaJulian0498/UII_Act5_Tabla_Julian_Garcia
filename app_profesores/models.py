from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.PositiveIntegerField()
    correo=models.EmailField(unique=True)

    #Es para el administrador servidor admin
    def __str__(self):
        return f"{self.nombre} {self.edad}"