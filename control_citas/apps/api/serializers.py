from rest_framework import serializers

from apps.paciente.models import Paciente
from apps.cita.models import Cita
from apps.doctor.models import Doctor


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            'nombre',
            'apellidos',
            'sexo',
            'edad',
            'alergias',
            'fecha_ingreso',
            'email',
        )
        read_only_fields = ('created_at', 'updated_at',)


class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = (
            'doctor',
            'paciente',
            'fecha_cita',
            'razones',
        )


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'nombre',
            'apellidos',
            'cedula',
            'telefono',
            'area',
            'comentario',
            'paciente',
        )
