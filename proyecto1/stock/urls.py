from django.urls import path
from stock.views import crear_insumo, crear_producto, atencion_al_cliente

urlpatterns = [
    path('atencion_al_cliente/', atencion_al_cliente, name = 'atencion_al_cliente'),
    path('crear_insumo/', crear_insumo, name = 'crear_insumo'), 
    path('crear_producto/', crear_producto, name='crear producto')
]