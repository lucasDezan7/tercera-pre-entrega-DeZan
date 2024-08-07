from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'Nombre:{self.nombre} | Camada:{self.camada}'

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField(max_length=40)

    def __str__(self):
        return f'Nombre:{self.nombre} | Apellido:{self.apellido}'
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField(max_length=40)

    def __str__(self):
        return f'Nombre del profesor:{self.nombre}'
   

