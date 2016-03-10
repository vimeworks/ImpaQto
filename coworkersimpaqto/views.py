from django.http import HttpResponse,JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from .serializers import ContratoSerializer, CoworkerSerializer
#from rest_framework import viewsets
from django.shortcuts import render
from .models import Coworker, Membresia, Contrato, ControlConsumo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistroCoworkerForm, RegistroMembresiaForm, RegistroContratosForm, EditarCoworkerForm,CoworkerEForm,EdicionMembresiaForm,EditarContratosForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.context import RequestContext
from django.db.models import  Sum


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
            minutos_mes= 60 * membresia.uso_espacio
            contrato_model = Contrato.objects.create(coworker=coworker,membresia=membresia,fecha_inicio=fecha_inicio,estado=estado,minutos_mes=minutos_mes)
            contrato_model.save()
            return redirect(reverse('contrato.listado'))
    else:
        form = RegistroContratosForm()
    context = {'form' : form}
    return render(request,'coworkersimpaqto/registroContrato.html',context)


@login_required
def editar_dos_coworker(request,pk=None):
    #if request.coworker is None:
    coworker = get_object_or_404(Coworker,id=pk)
    request.coworker = coworker
    
    if request.method == 'POST':
        form = EditarCoworkerForm(request.POST)
        if form.is_valid():
            coworker = get_object_or_404(Coworker,id=pk)
            cleaned_data = form.cleaned_data
            coworker.id = cleaned_data.get('id')
            coworker.nombre = cleaned_data.get('nombre')
            coworker.apellido = cleaned_data.get('apellido')
            coworker.mail = cleaned_data.get('mail')
            coworker.username = cleaned_data.get('username')
            coworker.save()
            return redirect (reverse('coworker.listado'))
    else:
        coworker =get_object_or_404(Coworker,id=pk) 
        request.coworker = coworker 
        
        if coworker:
            form = EditarCoworkerForm(request.POST or None,initial={'id':request.coworker.id,'nombre':request.coworker.nombre,'apellido':request.coworker.apellido,'mail':request.coworker.mail,'username':request.coworker.username})
        else:
            form = EditarCoworkerForm(request.POST or None)
                                  
    return render(request, 'coworkersimpaqto/editarCoworker.html',{'form' : form,'coworker':coworker})

@login_required
def editar_membresia(request,pk=None):
    membresia = get_object_or_404(Membresia,id=pk)
    request.membresia=membresia
    if request.method == 'POST':
        form = EdicionMembresiaForm(request.POST)
        if form.is_valid():
            membresia = get_object_or_404(Membresia,id=pk)
            cleaned_data = form.cleaned_data
            #membresia.nombre= cleaned_data.get('nombre')
            membresia.estado = cleaned_data.get('estado')
            membresia.save()
            return redirect (reverse('membresia.listado'))
    else:
        membresia =get_object_or_404(Membresia,id=pk) 
        request.membresia = membresia 
        
        if membresia:
            form = EdicionMembresiaForm(request.POST or None,initial={'nombre':request.membresia.nombre,'uso_espacio':request.membresia.uso_espacio,'modalidad':request.membresia.modalidad,'estado':request.membresia.estado})
        else:
            form = EdicionMembresiaForm(request.POST or None)
                                  
    return render(request, 'coworkersimpaqto/edicion.html',{'form' : form,'membresia':membresia, 'titulo':'Membresia','retorno':'membresia.listado'})

@login_required
def editar_contrato(request,pk=None):
    contrato = get_object_or_404(Contrato,id=pk)
    request.contrato=contrato
    if request.method == 'POST':
        form = EditarContratosForm(request.POST)
        if form.is_valid():
            contrato = get_object_or_404(Contrato,id=pk)
            cleaned_data = form.cleaned_data
            contrato.estado = cleaned_data.get('estado')
            contrato.save()
            return redirect (reverse('contrato.listado'))
    else:
        contrato =get_object_or_404(Contrato,id=pk) 
        request.contrato = contrato 
        
        if contrato:
            form = EditarContratosForm(request.POST or None,initial={'coworker':request.contrato.coworker,'membresia':request.contrato.membresia,'estado':request.contrato.estado,'fecha_inicio':request.contrato.fecha_inicio})
        else:
            form = EditarContratosForm(request.POST or None)
                                  
    return render(request, 'coworkersimpaqto/edicion.html',{'form' : form,'contrato':contrato, 'titulo':'Contrato','retorno':'contrato.listado'})

@login_required
def reportes(request):
    response_data={}
    response_data['dias']=["1", "2", "3", "4", "5", "6", "7","8","9","10","11","12","13"]
    response_data['consumo']=[65, 59, 40, 51, 36, 25, 40,50,20,30,45,80,80]
    meses = ControlConsumo.objects.values('mes','control_minutos').annotate(suma=Sum('control_minutos'))
    response_data['mes']=meses
    return JsonResponse(response_data) #HttpResponse(json.dumps(response_data),content_type="application/json")

