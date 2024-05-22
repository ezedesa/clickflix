from django.urls import path
from . import views

urlpatterns = [

    path('index/<str:usuario>', views.bienvenido, name='index'),
    path('catalogo/',views.mostrar_catalogo, name="catalogo"),
    path('ver_pelicula/<str:id>', views.ver_pelicula, name='ver_pelicula'),
    path('validacion_compra/<str:id>', views.validacion_compra, name="validacion_compra"),
]