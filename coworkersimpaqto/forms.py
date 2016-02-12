from django import forms
from .models import Coworker, Membresia, Contrato
from _datetime import date
import datetime

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
    
class RegistroMembresiaForm(forms.Form):
    MODALIDAD_CHOICES=(
        ('D','Diario'),
        ('M','Mensual'),
        ('S','Semestral'),
        ('A','Anual'),
    )
    STATE_CHOICES=(
        ('A','Activo'),
        ('I','Inactivo'),
    )
    nombre = forms.CharField(min_length=3,
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de la membresia'}))
    uso_espacio = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    modalidad = forms.ChoiceField(choices=MODALIDAD_CHOICES,
                                  required=True,
                                  widget=forms.Select(attrs={'class': 'form-control m-b'}))
    estado = forms.ChoiceField(choices=STATE_CHOICES,
                               required=True,
                               widget=forms.Select(attrs={'class': 'form-control m-b'}))
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Membresia.objects.filter(nombre=nombre):
            raise forms.ValidationError('Ya existe el nombre como membresia.')
        return nombre 

class RegistroContratosForm(forms.Form):
    ACTIVO='A'
    INACTIVO='I'
    ESTADO_CHOICES=(
        (ACTIVO,'Permitida'),
        (INACTIVO,'Por definir'),
    )
    coworker = forms.ModelChoiceField(queryset=Coworker.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control m-b'}))
    membresia = forms.ModelChoiceField(queryset=Membresia.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control m-b'}))
    estado = forms.ChoiceField(label=u'Utilización de Espacio',choices=ESTADO_CHOICES,
                               required=True,
                               widget=forms.Select(attrs={'class': 'form-control m-b'}))
    fecha_inicio = forms.DateField(initial=datetime.date.today(),
                                   widget=forms.TextInput(attrs={'class': 'form-control','id':'datepicker'}))
    