from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def ver_pelicula(request,id):

    lista_peliculas = [
        {
            "id" : "1",
            "titulo" : "El reino del planeta de los simios",
            "director" : "Wes Ball", 
            "anio" : "2024",
            "sinopsis" : "Ambientada varias generaciones en el futuro tras el reinado de César, en la que los simios son la especie dominante que vive en armonía y los humanos se han visto reducidos a vivir en la sombra. Mientras un nuevo y tiránico líder simio construye su imperio, un joven simio emprende un angustioso viaje que le llevará a cuestionarse todo lo que sabe sobre el pasado y a tomar decisiones que definirán el futuro de simios y humanos por igual.", 
            "precio" : "29.99",
            "genero" : ["ciencia ficcion","accion","aventura"],
            "duracion" : "2hs 25min", 
        },
        {
            "id" : "2",
            "titulo" : "Oppenheimer",
            "director" : "Christopher Nolan", 
            "anio" : "2023",
            "sinopsis" : "Película sobre el físico J. Robert Oppenheimer y su papel como desarrollador de la bomba atómica. Basada en el libro 'American Prometheus: The Triumph and Tragedy of J. Robert Oppenheimer' de Kai Bird y Martin J. Sherwin.", 
            "precio" : "24.99",
            "genero" : ["Drama","Historica"],
            "duracion" : "3hs 1m", 
        },
        {
            "id" : "3",
            "titulo" : "Guerra Civil",
            "director" : "Alex Garland", 
            "anio" : "2024",
            "sinopsis" : "En un futuro cercano donde América está sumida en una cruenta guerra civil, un equipo de periodistas y fotógrafos de guerra emprenderá un viaje por carretera en dirección a Washington DC. Su misión: llegar antes de que las fuerzas rebeldes asalten la Casa Blanca y arrebaten el control al presidente de los Estados Unidos.", 
            "precio" : "29.99",
            "genero" : ["Belica" , "Accion"],
            "duracion" : "1h 49m", 
        },
        {
            "id" : "4",
            "titulo" : "Garfield",
            "director" : "Mark Dindal", 
            "anio" : "2024",
            "sinopsis" : "El mundialmente famoso Garfield, el gato casero que odia los lunes y que adora la lasaña, está a punto de vivir una aventura ¡en el salvaje mundo exterior! Tras una inesperada reunión con su largamente perdido padre – el desaliñado gato callejero Vic – Garfield y su amigo canino Odie se ven forzados a abandonar sus perfectas y consentidas vidas al unirse a Vic en un hilarante y muy arriesgado atraco.", 
            "precio" : "19.99",
            "genero" : ["Animacion"],
            "duracion" : "1h 41m", 
        },
    ]
    for pelicula in lista_peliculas :
        if(pelicula["id"] == id):
            context = pelicula 

    return render(request, 'web/ver_pelicula.html', {"pelicula": context})