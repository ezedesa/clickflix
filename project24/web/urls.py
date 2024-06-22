from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/login.html"), name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),

    # CRUD PELICULAS
    path('catalogo', views.MoviesListView.as_view(), name="catalogo"),
    path('add_movie/', views.MoviesCreateView.as_view(), name="add_movie"),
    path('update_movie/<int:pk>/', views.PeliculaUpdateView.as_view(), name='update_movie'), path('delete_movie/<int:pk>/', views.MoviesDelete.as_view(), name="delete_movie"),
    path('ver_pelicula/<int:id>', views.ver_pelicula, name='ver_pelicula'),
    path('validacion_compra/<int:id>/', views.validacion_compra, name="validacion_compra"),

    path('mis_peliculas/', views.MyMovies.as_view(), name="mis_peliculas"),

]