from django.contrib import admin

from apps.paciente.models import Paciente


# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass