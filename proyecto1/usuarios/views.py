from django.shortcuts import render, redirect
from usuarios.forms import UsuarioFormulario
from usuarios.models import Usuario, Venta
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
########################## CRUD USUARIOS########################
@login_required(login_url='login')
def crear_usuario(request): 
    if request.method == "POST": 
        mi_formulario = UsuarioFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario = Usuario(
                nombre=informacion["nombre"],
                dni=informacion["dni"], 
                email=informacion["email"],
                empresa=informacion["empresa"]
            )
            
            usuario.save()
            return render(request, 'index.html')
        else:
            return render(request, 'usuario_formulario.html', {"usuario": usuario})
    else:
        usuario = UsuarioFormulario()
        return render(request, 'usuario_formulario.html', {"usuario": usuario})
 #----------------------------------------------------------------------------------------------   
def leer_Usuarios(request):
    lista_Usuario = Usuario.objects.all()
    return render(request, "leer_usuarios.html", {"usuarios": lista_Usuario})
#-----------------------------------------------------------------------------------------------
def eliminar_usuarios(request, nombre_usuario): 
    usuario = Usuario.objects.get(nombre=nombre_usuario)
    usuario.delete()
    return redirect('leer usuarios')
#-----------------------------------------------------------------------------------------------
def editar_usuario(request, nombre_usuario): 
    usuario = Usuario.objects.get(nombre=nombre_usuario)
    
    if request.method == "POST": 
        formulario = UsuarioFormulario(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.nombre = informacion['nombre']
            usuario.dni = informacion['dni']
            usuario.email = informacion['email']
            usuario.empresa = informacion['empresa']
            usuario.save()
            return render(request, "index.html")
    else:
        formulario = UsuarioFormulario()
        return render(request, "editar_usuarios.html", {"formulario": formulario})
    #-------------------------------------------------------------------------------------
    
    ################### CRUD VENTAS ##########################
    
class VentaListView(ListView):
    model = Venta
    context_object_name = "ventas"
    template_name = "ventas_lista.html"

class VentaCreateView(CreateView):
    model = Venta
    template_name = "ventas_crear.html"
    success_url = reverse_lazy('ventas_lista')
    fields = ['usuario', 'nro_transaccion', 'producto', 'cantidad', 'fecha']

class VentaUpdateView(UpdateView): 
    model = Venta
    template_name = "ventas_editar.html"
    fields = ['producto', 'canitdad', 'fecha_de_venta']

class VentaDeleteView(DeleteView):
    model = Venta 
    template_name = "ventas_eliminar.html"
    success_url = reverse_lazy("ventas lista")