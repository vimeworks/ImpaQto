from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from .serializers import ContratoSerializer, CoworkerSerializer
#from rest_framework import viewsets
from django.shortcuts import render
from .models import Coworker, Membresia, Contrato
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistroCoworkerForm, RegistroMembresiaForm, RegistroContratosForm, EditarCoworkerForm,CoworkerEForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.context import RequestContext

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
   CreateView,
   UpdateView,
   DeleteView
)
from django import forms

class CoworkerUpdate(UpdateView):
    model = Coworker
    form_class=EditarCoworkerForm
    success_url = reverse_lazy('coworker.listado')
    #fields = ['nombre', 'apellido', 'mail', 'username']


# Create your views here.

@login_required
def index(request):
    nombre = request.user.username
    context={'nombre':nombre}
    return render(request,'coworkersimpaqto/index.html',context)

@login_required
def coworker(request):
    #if user.is_authenticated():
        nombre = request.user.username
        coworker = Coworker.objects.all()
        context={'nombre':nombre, 'coworkers': coworker}
        return render(request,'coworkersimpaqto/coworkerlist.html',context)
    #else:
        #mensaje='No esta autenticado:'+request.user.username
        #return render(request,'accounts/login.html',{'mensaje':mensaje})

@login_required
def list_membresia_view(request):
    membresia = Membresia.objects.all()
    context = {'membresias':membresia}
    return render(request,'coworkersimpaqto/membresialist.html',context)

@login_required
def registro_coworker_view(request):
    if request.method == 'POST':
        form = RegistroCoworkerForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            nombre = cleaned_data.get('nombre')
            apellido = cleaned_data.get('apellido')
            mail = cleaned_data.get('mail')
            coworker_model = Coworker.objects.create(nombre=nombre,apellido=apellido)
            coworker_model.mail = mail
            coworker_model.username = username
            coworker_model.save()
            return redirect(reverse('coworker.listado'))
    else:
        form = RegistroCoworkerForm()
    context = {'form' : form}
    return render(request,'coworkersimpaqto/registroCoworker.html',context)

@login_required 
def registro_membresia_view(request):
    if request.method == 'POST':
        form = RegistroMembresiaForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            uso_espacio = cleaned_data.get('uso_espacio')
            modalidad = cleaned_data.get('modalidad')
            estado = cleaned_data.get('estado')
            membresia_model =  Membresia.objects.create(nombre=nombre,uso_espacio=uso_espacio,modalidad=modalidad,estado=estado)
            membresia_model.save()
            return redirect(reverse('membresia.listado'))
    else:
        form = RegistroMembresiaForm()
    context = {'form' : form}
    return render(request,'coworkersimpaqto/registroMembresia.html',context)

@login_required
def list_contratos_view(request):
    contrato = Contrato.objects.all()
    context = {'contratos':contrato}
    return render(request,'coworkersimpaqto/contratoList.html',context)

@login_required
def registro_contrato_membresia_view(request):
    if request.method == 'POST':
        form = RegistroContratosForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            coworker = cleaned_data.get('coworker')
            membresia =  cleaned_data.get('membresia')
            fecha_inicio = cleaned_data.get('fecha_inicio')
            estado = cleaned_data.get('estado')
            contrato_model = Contrato.objects.create(coworker=coworker,membresia=membresia,fecha_inicio=fecha_inicio,estado=estado)
            contrato_model.save()
            return redirect(reverse('contrato.listado'))
    else:
        form = RegistroContratosForm()
    context = {'form' : form}
    return render(request,'coworkersimpaqto/registroContrato.html',context)

@login_required
def editar_coworker(request,pk=None):
    #if request.coworker is None:
    coworker = Coworker.objects.filter(pk=pk)
    request.coworker = coworker
    
    if request.method == 'POST':
        form = CoworkerEForm(request.POST)
        if form.is_valid():
            '''request.coworker.nombre = form.cleaned_data['nombre']
            request.coworker.apellido = form.cleaned_data['apellido']
            request.coworker.mail = form.cleaned_data['mail']
            request.coworker.username = form.cleaned_data['username']
            request.coworker.save()'''
            cleaned_data = form.cleaned_data
            coworker.nombre = cleaned_data.get('nombre')
            coworker.save()
            return redirect (reverse('coworker.listado'))
    else:
        coworker = Coworker.objects.filter(pk=3)
        request.coworker = coworker #EditarCoworkerForm(request=request)
        form = CoworkerEForm(request=request,instance=coworker)
                                  #initial={'nombre':request.coworker.nombre,'apellido':request.coworker.apellido,'mail':request.coworker.mail,'username':request.coworker.username}
                                  #)
    return render(request, 'coworkersimpaqto/editarCoworker.html',{'form' : form})


@login_required
def editar_dos_coworker(request,pk=None):
    #if request.coworker is None:
    coworker = get_object_or_404(Coworker,id=pk)
    request.coworker = coworker
    doce=''
    if request.method == 'POST':
        form = EditarCoworkerForm(request.POST)
        if form.is_valid():
            '''coworker.nombre = form.cleaned_data['nombre']
            coworker.apellido = form.cleaned_data['apellido']
            coworker.mail = form.cleaned_data['mail']
            coworker.username = form.cleaned_data['username']
            coworker.save()'''
            coworker = get_object_or_404(Coworker,id=pk)
            cleaned_data = form.cleaned_data
            coworker.nombre = cleaned_data.get('nombre')
            coworker.apellido = cleaned_data.get('apellido')
            coworker.mail = cleaned_data.get('mail')
            coworker.username = cleaned_data.get('username')
            coworker.save()
            return redirect (reverse('coworker.listado'))
    else:
        coworker =get_object_or_404(Coworker,id=pk) #Coworker.objects.filter(pk=3)
        request.coworker = coworker #EditarCoworkerForm(request=request)
        doce='uno'
        if coworker:
            doce=pk
            form = EditarCoworkerForm(request.POST or None,initial={'id':request.coworker.id,'nombre':request.coworker.nombre,'apellido':request.coworker.apellido,'mail':request.coworker.mail,'username':request.coworker.username})
        else:
            doce='dos'
            form = CoworkerEForm(request.POST or None)                      #initial={'nombre':request.coworker.nombre,'apellido':request.coworker.apellido,'mail':request.coworker.mail,'username':request.coworker.username}
                                  #)
    return render(request, 'coworkersimpaqto/editarCoworker.html',{'form' : form,'coworker':coworker,'doce':doce})
