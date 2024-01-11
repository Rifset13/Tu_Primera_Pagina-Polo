from django import forms

class InsumoFormulario(forms.Form): 
    nombre = forms.CharField()
    descripcion = forms.CharField()
    cantidad_en_stock = forms.IntegerField()
    
class AtencionFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion_del_problema = forms.CharField()
    descripcion_del_problema = forms.CharField()