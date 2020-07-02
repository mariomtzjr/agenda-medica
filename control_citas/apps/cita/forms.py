from django import forms

from apps.paciente.models import Paciente


class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject',}))
    message = forms.CharField(widget=forms.Textarea(
                              attrs={'class':'form-control w-50'}))
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=Paciente.objects.all(),
                                           widget=forms.SelectMultiple())
