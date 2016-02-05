from django.shortcuts import render
from .models import Coworker
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistroCoworkerForm
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