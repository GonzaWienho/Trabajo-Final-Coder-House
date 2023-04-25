from django.contrib import admin
from hola_mundo.models import Usuarios,lista_de_entregas,stock_local

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(lista_de_entregas)
admin.site.register(stock_local)