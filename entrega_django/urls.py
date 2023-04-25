"""
URL configuration for entrega_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hola_mundo.views import (mostrar_template, mostrar_usuarios,
 mostrar_entregas, mostrar_stock,cargar_usuario, buscar_usuario,cargar_entregas
 ,cargar_stock)
from Hamgurga.views import (index,PostList,PostDetail, PostCreate,PostUpdate, PostDelete, SignUp,Login, Logout)

urlpatterns = [
    path('',index, name="index"),
    path('admin/', admin.site.urls),
    path('mi-template',mostrar_template),
    path('Usuarios', mostrar_usuarios, name= "Mis-usuarios"),
    path('Usuarios/formulario',cargar_usuario, name="Formulario-Users"),
    path('Usuarios/lista',buscar_usuario.as_view(), name="List-Users"),
    path('stock',mostrar_stock),
    path('stock/formulario',cargar_stock),
    path('entregas',mostrar_entregas),
    path('entregas/formulario',cargar_entregas, name="Formulario-Entregas"),
    path('post/lista',PostList.as_view(), name="Post-List"),
    path('post/<pk>/detalle',PostDetail.as_view(), name="Post-Detail"),
    path('post/crear',PostCreate.as_view(), name="Post-Create"),
    path('post/<pk>/actualizar',PostUpdate.as_view(), name="Post-Update"),
    path('post/<pk>/borrar',PostDelete.as_view(), name="Post-Delete"),
    path('signup',SignUp.as_view(), name="Signup"),
    path('login',Login.as_view(), name="Login"),
    path('logout',Logout.as_view(), name="Logout"),

]
