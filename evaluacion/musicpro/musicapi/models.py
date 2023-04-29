from django.db import models

# Create your models here.

class Cliente (models.Model):
    id_cliente = models.BigIntegerField(9999,primary_key=True)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    correo = models.EmailField()
    direccion = models.CharField(max_length=40)
    def __str_ (self):
        return self.Id_cliente


class Vendedor (models.Model):
    id_vendedor = models.BigIntegerField(9999, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)
    correo = models.EmailField()
    password = models.CharField(max_length=50)

class Producto(models.model):
    id_producto = models.BigIntegerField(999,primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()

class Bodega(models.model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Pedido(models.model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    aprobado = models.BooleanField(default=False)
    despachado = models.BooleanField(default=False)

class Bodeguero(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    password = models.CharField(max_length=50)

class Pago(models.model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    confirmado = models.BooleanField(default=False)

class Contador(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    password = models.CharField(max_length=50)