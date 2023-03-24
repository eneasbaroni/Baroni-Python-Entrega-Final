from django.urls import path
from .views import list_clientes, create_cliente, edit_cliente, delete_cliente

urlpatterns = [
  path('list-clientes/', list_clientes),
  path('create-cliente/', create_cliente),
  path('edit-cliente/<int:id>', edit_cliente),
  path('delete-cliente/<int:id>', delete_cliente),  
]