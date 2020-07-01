from django.db import models


# Create your models here.
class Paciente(models.Model):

    GENDER_CHOICES = [
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    ]
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    edad = models.IntegerField()
    alergias = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    domicilio = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)
