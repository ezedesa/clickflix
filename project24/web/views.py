from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .forms import MedioDePagoForm, PeliculaForm
from .models import Pelicula, Usuario, Transaccion
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError


# Create your views here.
def index(request):

    contexto = {}

    return render(request, 'web/index.html', contexto)

def user_logout(request):
    logout(request)

    messages.success(request, 'Sesion Cerrada')

    return redirect('index')

"""def bienvenido(request, usuario):
    context={
        'usuario':usuario
    }
    return render(request, 'web/index.html', context)
"""

def ver_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request, 'web/ver_pelicula.html', {'pelicula': pelicula})

## crud peliculas

#View clase que muestra el catalogo
class MoviesListView(ListView):
    model=Pelicula
    context_object_name='peliculas'
    template_name='web/catalogo.html'

#te lleva a la view para eliminar la pelicula
class MoviesDelete(DeleteView):
    model=Pelicula
    context_object_name='peliculas'
    template_name='web/eliminar_pelicula.html'
    success_url = reverse_lazy('catalogo')


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

class PeliculaUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Pelicula 
    template_name = "web/editar_pelicula.html"
    # specify the fields 
    form_class = PeliculaForm
    # can specify success url 
    success_url = reverse_lazy('catalogo')


@login_required
def validacion_compra(request,id):

    # la pelicula a comprar la traemos por id
    pelicula = Pelicula.objects.get(id_pelicula=id)
    # simula ser el usuario logeado
    usuario = Usuario.objects.get(id_usuario = request.user.id)

    if request.method == "GET":
        formulario = MedioDePagoForm(initial={'peliculas': pelicula})

    else:
        formulario = MedioDePagoForm(request.POST)
        
        if formulario.is_valid():
            formulario.instance.peliculas = pelicula
            formulario.instance.usuarios = usuario
            if Transaccion.objects.filter(usuarios=usuario, peliculas=pelicula).exists():
                messages.error(request, "Usted ya compro esta pelicula, no puede volver a comprarla")
            else:
                messages.success(request, 'Se compró con éxito ')
                formulario.save()
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')

    contexto = {
        'precio':pelicula.precio,
        'pelicula': pelicula,
        'formulario': formulario,
    }

    return render(request, 'web/validacion_compra.html', contexto)
