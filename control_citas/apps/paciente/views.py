from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from apps.api.serializers import PacienteSerializer
from apps.paciente.models import Paciente


# Create your views here.
class PacienteCreate(generics.CreateAPIView):
    serializer_class = PacienteSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'paciente/paciente_form.html'

    def get(self, request, *args, **kwargs):
        serializer = PacienteSerializer()
        return Response({'serializer': serializer})
    
    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('paciente_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PacienteListar(generics.ListAPIView):
    serializer_class = PacienteSerializer
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'paciente/paciente_list.html'

    def get(self, request, *args, **kwargs):
        queryset = Paciente.objects.all()
        serializer = PacienteSerializer(queryset, many=True)
        return Response({'serializer': serializer})


class PacienteUpdate(generics.UpdateAPIView):
    serializer_class = PacienteSerializer

    def post(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        serializer = PacienteSerializer(paciente, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'paciente': paciente})
        serializer.save()
        return redirect('paciente_listar')


class PacienteDelete(generics.DestroyAPIView):
    serializer_class = PacienteSerializer

    def get_object(self, pk):
        try:
            return Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        paciente = self.get_object(pk)
        paciente.delete()
        return redirect('paciente_listar')
