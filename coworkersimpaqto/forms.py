from django import forms
from .models import Coworker, Membresia, Contrato
from _datetime import date
import datetime
from django.forms.models import ModelForm
from django.utils.text import slugify

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

class EditarCoworkerForm(forms.Form):
    model = Coworker
    
    id= forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control','disabled': 'disabled',}))
    nombre = forms.CharField(min_length=2,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(min_length=6,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def __init__(self,*args,**kwargs):
        #self.username = kwargs.pop('username')
        return super(EditarCoworkerForm,self).__init__(*args,**kwargs)
    
    def clean_id(self):
        id=self.cleaned_data['id']
        def clean_mail(self):
            mail = self.cleaned_data['mail']
            existe = Coworker.objects.filter(mail=mail).exclude(id=id)
            if existe:
                raise forms.ValidationError('Ya existe ese mail en la base de datos.')
        return id
   
    def clean_nombre(self):
        nombre =  self.cleaned_data['nombre']
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        return apellido
    
    def clean_mail(self):
        #id = int(self.cleaned_data['id'])
        mail = self.cleaned_data['mail']
        #existe = Coworker.objects.filter(mail=mail).exclude(id=2)
        #if existe:
            #raise forms.ValidationError('Ya existe ese mail en la base de datos.')
        return mail
    
    
    def clean_username(self):
        username = self.cleaned_data['username']
        #id = id
        #existe=Coworker.objects.filter(username=username).exclude(id=2)
        #if existe:
            #raise forms.ValidationError('Ya existe ese username en la base de datos.')
        return username
    
    
class CoworkerEForm(ModelForm):
    class Meta:
        model=Coworker
        fields = ['id','nombre', 'apellido', 'mail', 'username']
        exclude=()    
