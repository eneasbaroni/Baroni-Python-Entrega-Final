from django.contrib import admin
from obras.models import Obra
from clientes.models import Cliente
from equipo.models import Equipo
from .models import CustomUser

admin.site.register(Obra)
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(CustomUser)
