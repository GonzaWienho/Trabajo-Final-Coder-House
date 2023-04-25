from django.db import models

class Usuarios(models.Model):

    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    nick_name = models.TextField(max_length=100)

    def __str__(self):
        return f"- Nombre: {self.nombre} - Apellido: {self.apellido} - NickName: {self.nick_name}"


class lista_de_entregas(models.Model):

    nombre_entrega=models.TextField(max_length=40)
    estado = models.CharField(max_length=40,default="Por Hacer")

    def terminado(self):
        self.estado = "Terminado"

    def proximamente(self):
        self.estado = "Proximamente"

    def __str__(self):
        return self.nombre_entrega

class stock_local(models.Model):

    nombre_producto = models.TextField(max_length=40)
    fecha_vencimiento = models.CharField(max_length=40)
    fecha_elaboracion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_producto

