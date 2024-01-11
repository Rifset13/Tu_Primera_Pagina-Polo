from django.shortcuts import render
from stock.models import Insumo, Productos, Atencion
from django.template import loader
from django.http import HttpResponse
from stock.forms import InsumoFormulario, AtencionFormulario
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")


# Create your views here.

def crear_insumo(request): 
    
    insumo = Insumo(nombre="Tornillo", descripcion="tipo alen", cantidad_en_stock=567)
    
    insumo.save()
    
    template = loader.get_template("creacion_insumo.html")
    
    doc = template.render({"nombre": insumo.nombre})
    
    return HttpResponse(doc)

#-----------------------------------------------------------------------------------------------------------

def crear_producto(request): 
    
    print("mostrar request.py:")
    print(request.POST)
    
    if request.method == "POST": 
        nuevo_producto = Productos(
            tipo = request.POST["nombre"], 
            descripcion = request.POST["descripcion"], 
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "index.html")
        
    return render(request, 'producto_formulario.html')

#------------------------------------------------------------------------------------------------------------------
def crear_insumo(request): 
    
    if request.method == "POST": 
        nuevo_formulario = InsumoFormulario(request.POST)
        
        if nuevo_formulario.is_valid(): 
            informacion = nuevo_formulario.cleaned_data 
            nuevo_insumo = Insumo(
                nombre=informacion["nombre"], 
                descripcion=informacion["descripcion"], 
                cantidad_en_stock=informacion["cantidad_en_stock"]
            )
            
            nuevo_insumo.save()
            return render(request, 'index.html')
        else: 
            return render(request, 'insumo_formulario.html', {"formulario": nuevo_formulario})
    else:
        nuevo_formulario = InsumoFormulario()
        return render(request, 'insumo_formulario.html', {"formulario": nuevo_formulario})
    
#--------------------------------------------------------------------------------------------------------------------------
def atencion_al_cliente(request): 
    
    if request.method == "POST": 
        nueva_solicitud = AtencionFormulario(request.POST)
        
        if nueva_solicitud.is_valid(): 
            informacion = nueva_solicitud.cleaned_data 
            nueva_solicitud = Atencion(
                nombre=informacion["nombre"], 
                descripcion_del_problema=informacion["descripcion_del_problema"], 
            )
            
            nueva_solicitud.save()
            return render(request, 'index.html')
        else: 
            return render(request, 'atencion_al_cliente.html', {"solicitud": nueva_solicitud})
    else:
        nueva_solicitud = AtencionFormulario()
        return render(request, 'atencion_al_cliente.html', {"solicitud": nueva_solicitud})
