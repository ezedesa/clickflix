from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def ver_pelicula(request):
    context = {
        "id" : "1",
        "titulo" : "El reino del planeta de los simios",
        "director" : "Wes Ball", 
        "anio" : "2024",
        "sinopsis" : "Ambientada varias generaciones en el futuro tras el reinado de César, en la que los simios son la especie dominante que vive en armonía y los humanos se han visto reducidos a vivir en la sombra. Mientras un nuevo y tiránico líder simio construye su imperio, un joven simio emprende un angustioso viaje que le llevará a cuestionarse todo lo que sabe sobre el pasado y a tomar decisiones que definirán el futuro de simios y humanos por igual.", 
        "precio" : "29.99",
        "genero" : ["ciencia ficcion","accion","aventura"],
        "duracion" : "2hs 25min", 
    }
    return render(request, 'web/ver_pelicula.html', {"pelicula": context})