from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from .serializers import ContratoSerializer, CoworkerSerializer
#from rest_framework import viewsets
from django.shortcuts import render
from .models import Coworker, Membresia, Contrato
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistroCoworkerForm, RegistroMembresiaForm, RegistroContratosForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse



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

'''
class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class CoworkerViewSet(viewsets.ModelViewSet):
    queryset = Coworker.objects.all()
    serializer_class = CoworkerSerializer

@csrf_exempt
def ContratoDetailViewSet(request,id):
    contrato = Contrato.objects.get(id=id)
    serializer_class = ContratoSerializer(contrato)
    return serializer_class.data
    
@csrf_exempt
def contrato_detail_view(request,codigo):
    try:
        contrato = Contrato.objects.get(id = codigo)
    except Contrato.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ContratoSerializer(contrato)
'''