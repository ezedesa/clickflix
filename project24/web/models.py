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

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100 ,verbose_name="Nombre")
    email = models.CharField(verbose_name="Email", unique=True)
    usuario = models.CharField(verbose_name="Usuario", unique=True)
    contrasenia = models.CharField(verbose_name="Contraseña", unique=True)
    lista_peliculas = models.ManyToManyField(Pelicula, through="Transaccion")
    #lista_peliculas = models.CharField(verbose_name="Lista Peliculas", null=True)

class Transaccion(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    medio_pago= models.CharField(verbose_name="Medio de pago")

    fecha = models.DateField(verbose_name="Fecha", auto_now_add=True, null=True)
    class Meta:
        unique_together = (('id_usuario', 'id_pelicula'),)
