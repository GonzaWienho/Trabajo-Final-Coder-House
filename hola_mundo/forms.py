from django import forms

class UsuariosForms(forms.Form):

    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nick_name = forms.CharField(max_length=100)

class EntregasForms(forms.Form):

    nombre_entrega=forms.CharField(max_length=40)
    estado = forms.CharField(max_length=40)

class StockForms(forms.Form):

    nombre_producto = forms.CharField(max_length=40)
    fecha_vencimiento = forms.CharField(max_length=40)
    fecha_elaboracion = forms.CharField(max_length=40)

class Busqueda_UsuariosForms(forms.Form):
    criterio_nombre =forms.CharField(max_length=100)
