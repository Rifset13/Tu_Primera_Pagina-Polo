from django.db import models

# Create your models here.

class Usuario(models.Model): 
    nombre = models.CharField(max_length=45)
    dni = models.IntegerField()
    email = models.EmailField()
    empresa = models.CharField(max_length=50, default="empresa")
    
    def __str__(self): 
        return self.nombre + ", DNI: " + str(self.dni)

class Venta(models.Model): 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ventas")
    nro_transaccion = models.IntegerField()
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    
    def __str__(self): 
        return "Venta nro: " + str(self.nro_transaccion)

