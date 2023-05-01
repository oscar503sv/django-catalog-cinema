from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(null= True, blank = True)
    biografia = models.TextField()
    imagen = ImageField(upload_to="director/images/")

    def __str__(self):
        return self.nombre + " " + self.apellidos