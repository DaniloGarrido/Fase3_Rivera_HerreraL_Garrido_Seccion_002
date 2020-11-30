from django.contrib import admin

# Register your models here.
from . models import Producto, Marca,Compra, Categoria

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Compra)
admin.site.register(Categoria)
