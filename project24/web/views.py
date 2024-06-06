from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .datos import lista_peliculas

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import MedioDePagoForm, PeliculaForm
from .models import Pelicula

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


## crud peliculas

#View clase que muestra el catalogo
class MoviesListView(ListView):
    model=Pelicula
    context_object_name='peliculas'
    template_name='web/catalogo.html'


# View clase que agrega entradas(de peliculas) a la BBDD
class MoviesCreateView(CreateView):
    # model que usa para crear la view
    model = Pelicula
    # fichero html donde se renderiza la view
    template_name = "web/agregar_pelicula.html"
    # url donde se redirige una vez que clickeamos boton "submit"
    success_url = reverse_lazy('catalogo')
    # form que usa como base para mostrar en el html
    form_class = PeliculaForm


