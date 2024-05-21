from django.shortcuts import render
from django.http import HttpResponse
from .forms import MedioDePagoForm
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .datos import lista_peliculas




# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def compra_exitosa(request):
    """formulario=MedioDePagoForm()
    contexto = {
        'form_pago': formulario
    }
    if request.method == 'POST' and formulario.is_valid():

        messages.success(request, 'Compra exitosa')
        #return redirect('index')
    return render(request, 'web/compra_exitosa.html', contexto)"""
    contexto = {}

    if request.method == "GET":
        contexto['form_pago'] = MedioDePagoForm()
    
    else: # Asumo que es un POST
        form = MedioDePagoForm(request.POST)
        contexto['form_pago'] = form
        
        # Validar el form
        if form.is_valid():
            # Si el form es correcto
            # Lo redirijo a una vista segura por ejemplo el index
            
            messages.success(request, 'COMPRA EXITOSA')

            return redirect('compra_exitosa')
    return render(request, 'web/compra_exitosa.html', contexto)

def ver_pelicula(request, id):
    pelicula = next((p for p in lista_peliculas if p["id"] == id), None)
    return render(request, 'web/ver_pelicula.html', {"pelicula": pelicula})
	
def validacion_compra(request, id):
    pelicula = next((p for p in lista_peliculas if p["id"] == id), None)
    return render(request, 'web/validacion_compra.html', {"pelicula": pelicula})

def mostrar_catalogo(request):
    return render(request, 'web/catalogo.html', {"peliculas": lista_peliculas})
