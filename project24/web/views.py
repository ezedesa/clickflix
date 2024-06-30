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
from django.db.models import Prefetch


# Create your views here.
def index(request):

    contexto = {'current_view' : 'index'}

    return render(request, 'web/index.html', contexto)

def user_logout(request):
    logout(request)

    messages.success(request, 'Sesion Cerrada')

    return redirect('index')

def ver_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request, 'web/ver_pelicula.html', {'pelicula': pelicula, 'current_view' : 'ver_pelicula'})

## crud peliculas

# muestra el catalogo
class MoviesListView(ListView):
    model=Pelicula
    context_object_name='peliculas'
    template_name='web/catalogo.html'

class MoviesDelete(DeleteView):
    model=Pelicula
    context_object_name='peliculas'
    template_name='web/eliminar_pelicula.html'
    success_url = reverse_lazy('catalogo')

class MoviesCreateView(CreateView):
    model = Pelicula
    template_name = "web/agregar_pelicula.html"
    success_url = reverse_lazy('catalogo')
    form_class = PeliculaForm

class PeliculaUpdateView(UpdateView): 
    model = Pelicula 
    template_name = "web/editar_pelicula.html"
    form_class = PeliculaForm
    success_url = reverse_lazy('catalogo')

@login_required
def mis_peliculas(request):
    usuario = Usuario.objects.get(user_id = request.user.id)  
    context = {'usuario': usuario,
                'current_view' : 'mis_peliculas'
                }
    return render(request, 'web/mis_peliculas.html', context)

@login_required
def validacion_compra(request,id):
    pelicula = Pelicula.objects.get(id_pelicula=id)
    usuario = Usuario.objects.get(user_id = request.user.id)

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
        'current_view' : 'validacion_compra'
    }

    return render(request, 'web/validacion_compra.html', contexto)