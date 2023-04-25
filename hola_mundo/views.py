from django.shortcuts import render
from hola_mundo.models import Usuarios,stock_local,lista_de_entregas
from hola_mundo.forms import UsuariosForms,EntregasForms, StockForms, Busqueda_UsuariosForms
from django.views.generic import ListView

# Create your views here.

def mostrar_template(request):
    return render(request,"hola_mundo/index.html")

def mostrar_usuarios(request):
    index = Usuarios.objects.all()
    context = {
        "index": index,
        "form":UsuariosForms(),
    }
    return render(request,"hola_mundo/index.html", context)

def cargar_usuario(request):

    f=UsuariosForms(request.POST)
    index = Usuarios.objects.all()

    context = {
        "index": index,
        "form":f,
    }
    
    if f.is_valid():
        Usuarios(nombre=f.data["nombre"], apellido=f.data["apellido"],nick_name= f.data["nick_name"]).save()
        
    return render(request,"hola_mundo/Formulario.html", context)

def mostrar_stock(request):
    pag3 = stock_local.objects.all()
    return render(request, "hola_mundo/pag3.html",{"pag3": pag3})

def cargar_stock(request):

    f=StockForms(request.POST)
    pag3 = stock_local.objects.all()

    context = {
        "pag3": pag3,
        "form":f,
    }
    
    if f.is_valid():
        stock_local(nombre_producto=f.data["nombre_producto"], fecha_vencimiento=f.data["fecha_vencimiento"],fecha_elaboracion=f.data["fecha_elaboracion"]).save()

    return render(request, "hola_mundo/Formulario.html",context)

def mostrar_entregas(request):
    pag2 = lista_de_entregas.objects.all()
    return render(request, "hola_mundo/pag2.html",{"pag2": pag2})

def cargar_entregas(request):

    f=EntregasForms(request.POST)
    pag2 = lista_de_entregas.objects.all()

    context = {
        "pag2": pag2,
        "form":f,
    }
    
    if f.is_valid():
        lista_de_entregas(nombre_entrega=f.data["nombre_entrega"], estado=f.data["estado"]).save()

    return render(request, "hola_mundo/Formulario.html",context)

class buscar_usuario(ListView):
    model = Usuarios
    context_objet_name = "Usuarios_list.html"

    def get_queryset(self):
        f= Busqueda_UsuariosForms(self.request.GET)
        if f.is_valid():
            return Usuarios.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Usuarios.objects.none()

