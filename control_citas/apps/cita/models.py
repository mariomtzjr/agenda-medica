from django.db import models

from doctor.models import Doctor
from paciente.models import Paciente


# Create your models here.
class Cita(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    paciente = models.ForeignKey(
        Paciente,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    fecha_cita = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    razones = models.TextField()

    class Meta:
        verbose_name = "cita"
        verbose_name_plural = "citas"
