from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/',views.mostrar_catalogo, name="catalogo")
]
