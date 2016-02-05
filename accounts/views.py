from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .forms import RegistroUserForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages

# Create your views here.

@login_required
def index_view(request):
    return render(request,'coworkersimpaqto/index.html')

def login_view(request):
    if request.user.is_authenticated():
        return render(request,'coworkersimpaqto/index.html',{'nombre':username})
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'coworkersimpaqto/index.html',{'nombre':username})
            else:
                mensaje = 'Usuario se encuentra inactivo.'
                return render(request,'accounts/login.html',{'mensaje':mensaje})
        mensaje = 'Nombre de usuario o contraseña no valido.'
    return render(request,'accounts/login.html',{'mensaje':mensaje})

def logout_view(request):
    logout(request)
    messages.success(request,'Te has desconectado con exito.')
    return redirect(reverse('accounts.login'))

@login_required
def registro_usuario_view(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST,request.FILES)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            photo = cleaned_data.get('photo')
            user_model = User.objects.create_user(username=username, email=email, password=password)
            user_model.save()
            user_profile = UserProfile()
            user_profile.user = user_model
            user_profile.photo = photo
            user_profile.save()
            #return redirect(reverse('index'),kwargs={'nombre':username})
            return redirect(reverse('accounts.listado.userprofile'))
            
    else:
        form = RegistroUserForm()
    context = {
               'form' : form
               }
    return render(request,'accounts/registrousuario.html',context)

@login_required
def list_usuarios_view(request):
    userprofiles = UserProfile.objects.all()
    context={'userprofiles': userprofiles}
    return render(request,'accounts/listUser.html',context)
