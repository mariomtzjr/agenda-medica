from django.contrib import admin

from apps.cita.models import Cita


# Register your models here.
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    pass
