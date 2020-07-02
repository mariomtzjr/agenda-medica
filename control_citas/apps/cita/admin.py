from django.contrib import admin
from django.shortcuts import render

from apps.cita.models import Cita
from apps.cita.forms import SendEmailForm


def send_email(self, request, queryset):
    form = SendEmailForm(initial={'pacientes': queryset})
    return render(request, 'cita/send_email.html', {'form': form})


# Register your models here.
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    actions = [send_email]
    send_email.short_description = "Send an email to selected patients"
