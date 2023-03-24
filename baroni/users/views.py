from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.views import LogoutView, LoginView 
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth.views import PasswordChangeView

from .models import CustomUser
from django.urls import reverse_lazy

#Funcion para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else :
            print(form.errors)
            context = {
                'form': form,
                'message': form.errors
                }
            return render(request, 'usuarios/register.html', context)
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})


#clase basada en vistas para ver el perfil del usuario
class UserView(LoginRequiredMixin, TemplateView): #Hereda de TemplateView y LoginRequiredMixin (mixin para requerir login)
    template_name = 'usuarios/profile.html'

    def get_context_data(self, **kwargs): #sobreescribe el metodo get_context_data de TemplateView para pasarle el usuario
        context = super().get_context_data(**kwargs) 
        context['user'] = self.request.user
        return context  

#Clase basada en vistas para login
class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('login_status')
    def get_success_url(self):
        return reverse_lazy('login_status') 

#Funcion para ver el perfil del usuario
@login_required #decorador para que solo los usuarios logueados puedan ver el perfil, si no estan logueados se redirige a la pagina de login
def login_status(request):    
    return render(request, 'usuarios/login_status.html')    
    
#Clase basada en vistas para logout
class CustomLogoutView(LogoutView): #Hereda de LogoutView y sobreescribe el metodo get_next_page
    next_page = 'logout_exit'  # Página a la que redireccionar después del logout

#vista de Exito al cerrar sesion
def logout_exit(request):
    return render(request, 'usuarios/logout_view.html')

#Clase basada en vistas para actualizar el perfil del usuario
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'usuarios/update_user.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user 

#funciones para cambio de contraseña
class CustomPasswordChangeView(PasswordChangeView, LoginRequiredMixin):
    template_name = 'usuarios/change_password.html'
    success_url = reverse_lazy('password_status')

#vista de Exito al cerrar sesion
def password_status(request):
    return render(request, 'usuarios/password_status.html')