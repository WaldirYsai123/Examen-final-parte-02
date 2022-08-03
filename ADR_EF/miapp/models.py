from django.db import migrations, models

# Create your models here.
class Producto(models.Model):
    codigo = models.TextField(max_length=2)
    nombre = models.TextField()
    precio_compra = models.TextField()
    precio_venta = models.TextField()
    fecha_compra = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add = True)
    estado = models.CharField(max_length=1)