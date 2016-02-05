from django import forms
from .models import Coworker

class RegistroCoworkerForm(forms.Form):
    nombre = forms.CharField(min_length=2,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(min_length=6,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_username(self):
        """Comprueba que no exista un username igual en la bd"""
        username = self.cleaned_data['username']
        if Coworker.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username
    
    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['mail']
        if Coworker.objects.filter(mail=mail):
            raise forms.ValidationError('Ya existe un e-mail igual en la db.')
        return email
