from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required


""" funcion que lista los clientes """
@login_required #verificar que el usuario este logueado
def list_clientes(request):
    
  all_clientes = Cliente.objects.all()
    
  context = {
    'clientes': all_clientes
  }
  
  return render(request, 'clientes/list_clientes.html', context)

""" Funcion para crear clientes a traves de django forms """
@login_required #verificar que el usuario este logueado
def create_cliente(request):
  if request.method == 'GET':  
    form = ClienteForm()    
    return render(request, 'clientes/create_cliente.html', context={'form': form})
  else:
    form = ClienteForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Cliente.objects.create(name = data['name'], last_name = data['last_name'], email = data['email'], phone = data['phone'], address = data['address'], credit = data['credit'], active = data['active'])
      return render(request, 'clientes/create_cliente.html', context={})
    else:
      context = {
        'form': form,
        'message': form.errors #envio de errores para renderizar en html
      }
      return render(request, 'clientes/create_cliente.html', context)

#funcion para editar clientes
@login_required #verificar que el usuario este logueado
def edit_cliente(request, id):
  cliente = Cliente.objects.get(id=id)
  if request.method == 'GET':
    #obtener los daots del cliente y cargarlos en el formulario
    form = ClienteForm(initial={
      'name': cliente.name,
      'last_name': cliente.last_name,
      'email': cliente.email,
      'phone': cliente.phone,
      'address': cliente.address,
      'credit': cliente.credit,
      'active': cliente.active
      })     
    context = {
      'form': form ,
      'id': id,     
    }
    return render(request, 'clientes/edit_cliente.html', context)
  else:
    form = ClienteForm(request.POST)
    if form.is_valid():
      deta = form.cleaned_data
      Cliente.objects.filter(id=id).update(name = deta['name'], last_name = deta['last_name'], email = deta['email'], phone = deta['phone'], address = deta['address'], credit = deta['credit'], active = deta['active'])
      return render(request, 'clientes/edit_cliente.html', context={})      
    else:      
      context = {
        'form': form,
        'cliente': cliente,
        'message': form.errors,
        'id': id
      }
      return render(request, 'clientes/edit_cliente.html', context)

#funcion para eliminar clientes
@login_required #verificar que el usuario este logueado    
def delete_cliente(request, id):
  cliente = Cliente.objects.get(id=id)
  if request.method == 'GET':
    context = {
      'cliente': cliente
    }
    return render(request, 'clientes/delete_cliente.html', context)
  else:    
    cliente.delete()
    return render(request, 'clientes/delete_cliente.html', context={})
      


