from django.urls import path

from apps.paciente.views import (
    PacienteCreate,
    PacienteListar,
    PacienteUpdate,
    PacienteDelete
)

urlpatterns = [
    path('pacientes/crear', PacienteCreate.as_view(), name="paciente_crear"),
    path('pacientes/listar', PacienteListar.as_view(), name="paciente_listar"),
    path('pacientes/editar/<int:pk>', PacienteUpdate.as_view(), name="paciente_update"),
    path('pacientes/eliminar/<int:pk>', PacienteDelete.as_view(), name="paciente_delete")
]
