from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Movie(models.Model):
    director = models.ForeignKey('director.Director', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    duracion = models.PositiveIntegerField()
    imagen = ImageField(upload_to='movies/images/')
    anyo = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre