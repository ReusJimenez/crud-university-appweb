from django.db import models
from datetime import date

class Alumno(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    estado_estudio = models.BooleanField(default=True)

    class Meta:
        db_table = "alumno"

    @property
    def calcular_edad(self):
        today = date.today()
        edad = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad
    