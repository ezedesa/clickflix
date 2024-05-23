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
    return render(request, 'web/index.html', context)


def ver_pelicula(request, id):
    pelicula = next((p for p in lista_peliculas if p["id"] == id), None)
    return render(request, 'web/ver_pelicula.html', {"pelicula": pelicula})
	
def validacion_compra(request, id):
    pelicula = next((p for p in lista_peliculas if p["id"] == id), None)
    
    if request.method == 'POST':
        formulario = MedioDePagoForm(request.POST)
        if formulario.is_valid():
            messages.success(request, 'Compra exitosa')

        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        formulario = MedioDePagoForm()

    contexto = {
        'form_pago': formulario,
        'pelicula': pelicula
    }
    return render(request, 'web/validacion_compra.html', contexto)

def mostrar_catalogo(request):
    return render(request, 'web/catalogo.html', {"peliculas": lista_peliculas})