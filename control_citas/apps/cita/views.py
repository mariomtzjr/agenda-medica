from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from apps.api.serializers import CitaSerializer
from apps.cita.models import Cita
from apps.cita.forms import SendEmailForm


# Create your views here.
class CitaCreate(generics.CreateAPIView):
    serializer_class = CitaSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cita/cita_form.html'

    def get(self, request, *args, **kwargs):
        serializer = CitaSerializer()
        return Response({'serializer': serializer})
    
    def post(self, request):
        serializer = CitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('citas_listar')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CitaListar(generics.ListAPIView):
    serializer_class = CitaSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cita/cita_list.html'

    def get(self, request, *args, **kwargs):
        queryset = Cita.objects.all()
        serializer = CitaSerializer(queryset, many=True)
        return Response({'serializer': serializer})


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


# SendUserEmails view class
class CitaEmail(FormView):
    template_name = 'cita/send_email.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('admin:citas')

    def form_valid(self, form):
        users = form.cleaned_data['users']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(subject, message, '', users)
        user_message = '{0} users emailed successfully!'.format(form.cleaned_data['users'].count())
        messages.success(self.request, user_message)
        return super(CitaEmail, self).form_valid(form)