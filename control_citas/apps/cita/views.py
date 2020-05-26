from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics

from apps.api.serializers import CitaSerializer
from apps.cita.models import Cita


# Create your views here.
class CitaCreate(generics.CreateAPIView):
    serializer_class = CitaSerializer


class CitaListar(generics.ListAPIView):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()


class CitaUpdate(generics.UpdateAPIView):
    serializer_class = CitaSerializer

    def post(self, request, pk):
        cita = get_object_or_404(Cita, pk=pk)
        serializer = CitaSerializer(Cita, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'cita': cita})
        serializer.save()
        return redirect('cita_listar')


class CitaDelete(generics.DestroyAPIView):
    serializer_class = CitaSerializer

    def get_object(self, pk):
        try:
            return Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        cita = self.get_object(pk)
        cita.delete()
        return redirect('cita_listar')
