from django.contrib import admin
from stock.models import Insumo, Productos, Cliente, Atencion

# Register your models here.

admin.site.register(Insumo)
admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Atencion)