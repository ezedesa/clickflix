from django.db import models

# Create your models here.
from django.db import models
#
# Create your models here.

class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    director = models.CharField(verbose_name="Director")
    anio = models.CharField(verbose_name="Año")
    sinopsis = models.CharField(verbose_name="Sinopsis")
    precio = models.FloatField(verbose_name="Precio")
    genero = models.CharField(verbose_name="Género")
    duracion= models.CharField(verbose_name="Duración")
    imagen = models.ImageField(upload_to="images/",null=True,blank=True, default="movie-cover")

    def photo_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url

