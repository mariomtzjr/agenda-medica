from django.db import models
from apps.paciente.models import Paciente


# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    comentario = models.TextField()
    paciente = models.ForeignKey(
        Paciente,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctores"

    def __str__(self):
        return 'Dr. %s %s' % (self.nombre, self.apellidos)
