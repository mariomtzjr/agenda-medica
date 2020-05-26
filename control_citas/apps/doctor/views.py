from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics

from apps.api.serializers import DoctorSerializer
from apps.doctor.models import Doctor


# Create your views here.
class DoctorCreate(generics.CreateAPIView):
    serializer_class = DoctorSerializer


class DoctorListar(generics.ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorUpdate(generics.UpdateAPIView):
    serializer_class = DoctorSerializer

    def post(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(Doctor, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'doctor': doctor})
        serializer.save()
        return redirect('doctor_listar')


class DoctorDelete(generics.DestroyAPIView):
    serializer_class = DoctorSerializer

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        doctor = self.get_object(pk)
        doctor.delete()
        return redirect('doctor_listar')
