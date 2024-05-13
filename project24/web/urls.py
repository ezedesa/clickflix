from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('ver_pelicula', views.ver_pelicula, name='ver_pelicula')
]

