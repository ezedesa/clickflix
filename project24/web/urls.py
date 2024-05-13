from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('catalogo/',views.mostrar_catalogo, name="catalogo"),
    path('ver_pelicula/<str:id>', views.ver_pelicula, name='ver_pelicula')
]
