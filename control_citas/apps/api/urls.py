from django.urls import path

from apps.paciente.views import (
    PacienteCreate,
    PacienteListar,
    PacienteUpdate,
    PacienteDelete
)
from apps.cita.views import (
    CitaCreate,
    CitaListar,
    CitaUpdate,
    CitaDelete
)
from apps.doctor.views import (
    DoctorCreate,
    DoctorListar,
    DoctorUpdate,
    DoctorDelete
)

urlpatterns = [
    path('pacientes/crear', PacienteCreate.as_view(), name="paciente_crear"),
    path('pacientes/listar', PacienteListar.as_view(), name="paciente_listar"),
    path('pacientes/editar/<int:pk>', PacienteUpdate.as_view(), name="paciente_update"),
    path('pacientes/eliminar/<int:pk>', PacienteDelete.as_view(), name="paciente_delete"),

    path('citas/crear', CitaCreate.as_view(), name="cita_crear"),
    path('citas/listar', CitaListar.as_view(), name="cita_listar"),
    path('citas/editar/<int:pk>', CitaUpdate.as_view(), name="cita_update"),
    path('citas/eliminar/<int:pk>', CitaDelete.as_view(), name="cita_delete"),

    path('doctor/crear', DoctorCreate.as_view(), name="doctor_crear"),
    path('doctor/listar', DoctorListar.as_view(), name="doctor_listar"),
    path('doctor/editar/<int:pk>', DoctorUpdate.as_view(), name="doctor_update"),
    path('doctor/eliminar/<int:pk>', DoctorDelete.as_view(), name="doctor_delete"),



]