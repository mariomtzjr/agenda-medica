from rest_framework import serializers

from apps.paciente.models import Paciente
from apps.cita.models import Cita


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
