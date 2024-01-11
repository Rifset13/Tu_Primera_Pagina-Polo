from django import forms

class UsuarioFormulario(forms.Form): 
    nombre = forms.CharField(max_length=45)
    dni = forms.IntegerField()
    email = forms.EmailField()
    empresa = forms.CharField(max_length=50)
    