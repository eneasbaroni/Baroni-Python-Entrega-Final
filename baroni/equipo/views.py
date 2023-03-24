from django.shortcuts import render
from .models import Equipo
from .forms import MemberForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
#importar metodos para controlar login y permisos
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


#Listar equipo con clase basada en vistas
class list_members(ListView):
  model = Equipo
  template_name = 'equipo/list_equipo.html'
  context_object_name = 'equipo'

#Listar un miembro segun ID
class member_detail(DetailView):
  model = Equipo
  template_name = 'equipo/member_detail.html'
  context_object_name = 'member'

#Crear miembro con clase basada en vistas y validacion de formulario
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch') #permiso para superusuario
class create_member(CreateView):
  model = Equipo
  template_name = 'equipo/create_member.html'
  fields = ['name', 'last_name', 'email', 'phone', 'bio', 'position', 'image']
  success_url = '/equipo/list-equipo/'

#Editar miembro con clase basada en vistas y validacion de formulario
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch') #permiso para superusuario
class edit_member(UpdateView):
  model = Equipo
  template_name = 'equipo/edit_member.html'
  fields = ['name', 'last_name', 'email', 'phone', 'bio', 'position', 'image']
  success_url = '/equipo/list-equipo/' 

  #funcion para obtener imagen
  def form_valid(self, form):
    instance = form.save(commit=False)
    if 'image' in self.request.FILES:
        instance.image = self.request.FILES['image']
    instance.save()
    return super().form_valid(form)  
  

#Eliminar miembro con clase basada en vistas
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch') #permiso para superusuario
class delete_member(DeleteView):
  model = Equipo
  template_name = 'equipo/delete_member.html'
  context_object_name = 'member'
  success_url = '/equipo/list-equipo/' 