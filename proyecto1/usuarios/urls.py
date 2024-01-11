from django.urls import path
from usuarios.views import crear_usuario, leer_Usuarios, eliminar_usuarios, editar_usuario, VentaListView, VentaCreateView

urlpatterns = [
    path('crear_usuario/', crear_usuario, name='crear usuario'),
    path('leer_usuarios', leer_Usuarios, name= 'leer usuarios'),
    path("eliminar_usuario/<nombre_usuario>", eliminar_usuarios, name='eliminar usuario'), 
    path("editar_usuarios/<nombre_usuario>", editar_usuario, name='editar usuario'),
    path('ventas_lista/', VentaListView.as_view(), name='ventas_lista'),
    path('ventas_crear/', VentaCreateView.as_view(), name='ventas_crear')
]
