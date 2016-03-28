from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import RegistroUserForm, EditarUserForm
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
        return render(request,'coworkersimpaqto/index.html')
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

@login_required
def editar_accounts(request,pk=None):
    userProfile= get_object_or_404(UserProfile,id=pk)
    request.userProfile=userProfile
    if request.method == 'POST':
        form = EditarUserForm(request.POST)
        if form.is_valid():
            userProfile = get_object_or_404(UserProfile,id=pk)
            cleaned_data = form.cleaned_data
            password = form.cleaned_data['password']
            if password:
                user =  userProfile.user
                user.set_password(password)
                user.save();
            #photo = form.cleaned_data['photo']
            #if photo:
             #   userProfile.photo=photo
              #  userdos= userProfile.user
               # userdos.username = 'luis'
                #userdos.save()
                userProfile.save()
            return redirect (reverse('accounts.listado.userprofile'))
    else:
        userProfile =get_object_or_404(UserProfile,id=pk) 
        request.userProfile = userProfile 
        
        if userProfile:
            form = EditarUserForm(request.POST or None,initial={'username':request.userProfile.user.username,'email':request.userProfile.user.email,'password':request.userProfile.user.password,'password2':request.userProfile.user.password,'photo':request.userProfile.photo})
        else:
            form = EditarUserForm(request.POST or None)
                                  
    return render(request, 'accounts/edicion.html',{'form' : form,'userProfile':userProfile, 'titulo':'Editar Usuario','retorno':'accounts.listado.userprofile',})
