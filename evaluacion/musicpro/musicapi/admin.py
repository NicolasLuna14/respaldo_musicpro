from django.contrib import admin
from.models import Cliente
from.models import Vendedor
from.models import Producto
from.models import Carrito
from.models import Bodega
from.models import Sede
from.models import Pedido
from.models import DetallePedido
from.models import Bodeguero
from.models import Pago
from.models import Contador
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Bodega)
admin.site.register(Sede)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Bodeguero)
admin.site.register(Pago)
admin.site.register(Contador)
