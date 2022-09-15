from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    
    #se especifica que queremos representar en la bd, por ejempo en este caso el campo nombre
    def __str__(self):
        return self.nombre

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40, null=True)
    
    def __str__(self):
        return self.nombre

class Programador(models.Model):
    nombre = models.CharField(max_length=40)
    #llave foranea que mapea la tabla emrpresa
    edad = models.IntegerField(null = True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empleados") #la cascada sirve para eliminar algo de abajo por si algo de arriba tambien se elimina
    
    lenguaje = models.ManyToManyField(Lenguaje)
    
    def __str__(self):
        return self.nombre