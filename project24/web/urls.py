from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # CRUD PELICULAS
    path('catalogo', views.MoviesListView.as_view(), name="catalogo"),
    path('add_movie/', views.MoviesCreateView.as_view(), name="add_movie"),
    path('update_movie/<int:pk>/', views.PeliculaUpdateView.as_view(), name='update_movie'),
    path('delete_movie/<int:pk>/', views.MoviesDelete.as_view(), name="delete_movie"),

    path('index/<str:usuario>', views.bienvenido, name='index'),
    path('ver_pelicula/<int:id>', views.ver_pelicula, name='ver_pelicula'),
    path('validacion_compra/<int:id>/', views.validacion_compra, name="validacion_compra"),
]