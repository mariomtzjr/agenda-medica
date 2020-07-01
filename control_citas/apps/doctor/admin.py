from django.contrib import admin

from apps.doctor.models import Doctor


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass
