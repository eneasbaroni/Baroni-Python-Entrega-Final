from django.shortcuts import render
from .models import Obra
from .forms import ObraForm
#importar metodos para controlar login y permisos
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

#Funcion que lista las Obras 
def list_obras(request):
  #filtrar por busqueda
  if 'search' in request.GET:
    all_obras = Obra.objects.filter(name__icontains = request.GET.get('search'))
  else:
    all_obras = Obra.objects.all()
    
  context = {
    'obras': all_obras
  }
  return render(request, 'obras/list_obras.html', context)

def obra_detail(request, id):
  obra = Obra.objects.get(id = id)
  context = {
    'obra': obra
  }
  return render(request, 'obras/obra_detail.html', context)


#Funcion para crear Obra a traves de django forms
@login_required #verificar que el usuario este logueado
def create_obra(request):
  if request.method == 'GET':  
    form = ObraForm()    
    return render(request, 'obras/create_obra.html', context={'form': form})
  else:
    form = ObraForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      Obra.objects.create(name = data['name'], price = data['price'], area = data['area'], description = data['description'], credit = data['credit'], image = data['image'])
      return render(request, 'obras/create_obra.html', context={})
    else:
      context = {
        'form': form,
        'message': form.errors #envio de errores para renderizar en html
      }
      return render(request, 'obras/create_obra.html', context)
    
#Funcion para editar Obra
@login_required #verificar que el usuario este logueado
def edit_obra_NOUSAR(request, id): #NO SE UTILIZA PORQUE NO PRECARGA LA IMAGEN
  obra = Obra.objects.get(id=id)
  if request.method == 'GET':  
    form = ObraForm(initial={
      'name': obra.name,
      'price': obra.price,
      'area': obra.area,
      'description': obra.description,
      'credit': obra.credit,      
      'image': obra.image,
    })      
    context = {
      'form': form,
      'id': id,
    }
    return render(request, 'obras/edit_obra.html', context)
  else:
    form = ObraForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      obra.name = data['name']
      obra.price = data['price']
      obra.area = data['area']
      obra.description = data['description']
      obra.credit = data['credit']
      obra.image = data['image']
      obra.save()
      return render(request, 'obras/edit_obra.html', context={})
    else:
      context = {
        'form': form,
        'message': form.errors, #envio de errores para renderizar en html
        'id': id,
      }
      return render(request, 'obras/edit_obra.html', context)

#Editar obra con clase basada en vistas y validacion de formulario
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch') #permiso para superusuario
class edit_obra(UpdateView):
  model = Obra  
  template_name = 'obras/edit_obra.html'
  fields = ['name', 'price', 'area', 'description', 'credit', 'image']
  success_url = '/obras/list-obras/'

    
#Funcion para eliminar Obra
@login_required #verificar que el usuario este logueado
def delete_obra(request, id):
  obra = Obra.objects.get(id=id)
  if request.method == 'GET':
    context = {
      'obra': obra,      
    }
    return render(request, 'obras/delete_obra.html', context)
  else:
    obra.delete()
    return render(request, 'obras/delete_obra.html', context={})

    

   
    



# Create your views here.
