from django.urls import path
from .views import list_obras, obra_detail, create_obra, edit_obra, delete_obra 

urlpatterns = [
  path('list-obras/', list_obras),
  path('obra-detail/<int:id>', obra_detail),
  path('create-obra/', create_obra),
  #path('edit-obra/<int:id>', edit_obra),
  path('edit-obra/<int:pk>', edit_obra.as_view()),
  path('delete-obra/<int:id>', delete_obra),
   
  #Rutas Pendientes
]