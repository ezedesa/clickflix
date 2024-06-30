from django.db import models
from project24 import settings 


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

    def __str__(self) -> str:
        return self.titulo
    
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100 ,verbose_name="Nombre")
    email = models.CharField(verbose_name="Email", unique=True)
    lista_peliculas = models.ManyToManyField(Pelicula, through="Transaccion")

    user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		null=True,
		blank=True	
	)    

    def __str__(self) -> str:
        return self.user.username

class Transaccion(models.Model):
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    peliculas = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    CHOICES = [('tarjeta', 'Tarjeta de crédito'),('tarjeta', 'Tarjeta de débito')]

    medio_pago = models.CharField(choices=CHOICES)
    numero_tarjeta= models.CharField(verbose_name="Numero tarjeta", null=True, max_length=16)

    class Meta:
        unique_together = (('usuarios', 'peliculas'),)
    
    def __str__(self):
        return f" Usuario: {self.usuarios} | Pelicula: {self.peliculas}"