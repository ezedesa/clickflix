from django.shortcuts import render
from django.http import HttpResponse
from .forms import MedioDePagoForm
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .datos import lista_peliculas

# Create your views here.

def bienvenido(request, usuario):
    context={
        'usuario':usuario
    }
    return render(request, 'web/bienvenido.html', context)

def compra_exitosa(request):
    formulario=MedioDePagoForm()
    contexto = {
        'form_pago': formulario
    }
    if request.method == 'POST':

        messages.success(request, 'Compra exitosa')
    return render(request, 'web/compra_exitosa.html', contexto)


def ver_pelicula(request, id):
    pelicula = next((p for p in lista_peliculas if p["id"] == id), None)
    return render(request, 'web/ver_pelicula.html', {"pelicula": pelicula})
	
def validacion_compra(request, id):
    pelicula = next((p for p in lista_peliculas if p["id"] == id), None)
    return render(request, 'web/validacion_compra.html', {"pelicula": pelicula})

def mostrar_catalogo(request):
    return render(request, 'web/catalogo.html', {"peliculas": lista_peliculas})