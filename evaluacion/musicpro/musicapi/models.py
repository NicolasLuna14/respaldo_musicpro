from django.db import models

# Create your models here.

class Cliente (models.Model):
    id_cliente = models.BigIntegerField(9999,primary_key=True)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    correo = models.EmailField()
    direccion = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre


class Vendedor (models.Model):
    id_vendedor = models.BigIntegerField(9999, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)
    correo = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.model):
    id_producto = models.BigIntegerField(999,primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='productos')
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.producto

class Bodega(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.cantidad

class Sede(models.Model):
    direccion = models.CharField(200)
    numero_telefono = models.BigIntegerField(9)
    def __str__(self):
        return self.direccion

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20, choices=(('PENDIENTE', 'Pendiente'),('APROBADO','Aprobado'),('RECHAZADO','Rechazado')),default='PENDIENTE')
    #aprobado = models.BooleanField(default=False)
    #despachado = models.BooleanField(default=False)
    def __str__(self):
        return self.estado

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.producto

class Bodeguero(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Pago(models.model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    #confirmado = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.DecimalField(max_length=20, choices=(('TARJETA','Tarjeta de crédito'),('TRANSFERENCIA','Transferencia')),default='TARJETA')
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.pedido

class Contador(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre




