from rest_framework import serializers

from apps.paciente.models import Paciente


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
