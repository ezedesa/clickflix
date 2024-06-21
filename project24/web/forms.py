from django import forms
from django.core.exceptions import ValidationError
from .models import Pelicula,Transaccion,Usuario
from django.contrib.auth.models import User 

"""class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario')
    clave = forms.CharField(label='Contraseña')
"""    
# crea un form  que hereda de una clase "wrapper" de modelos para crear forms
class PeliculaForm (forms.ModelForm):
    class Meta:
        # de que modelo crea el form
        model = Pelicula
        # que campos muestra el form
        fields = ['titulo', 'director', 'anio', 'sinopsis', 'precio', 'genero','duracion','imagen']

    # fx que chequea si el anio tiene 4 "digitos"
    def clean_anio(self):
        if not len(self.cleaned_data["anio"]) == 4:
            raise ValidationError("Indique un año de 4 digitos.")
        return self.cleaned_data["anio"]


class MedioDePagoForm(forms.ModelForm):
    class Meta:
        model= Transaccion
        fields=['medio_pago','numero_tarjeta','usuarios','peliculas']
        exclude = ['usuarios','peliculas']
    
    def clean_numero_tarjeta(self):
        numero_tarjeta = self.cleaned_data["numero_tarjeta"]
        if not numero_tarjeta.isdigit() or len(numero_tarjeta) != 16:
            raise ValidationError("El número de tarjeta debe ser de 16 dígitos.")

        return self.cleaned_data["numero_tarjeta"]
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     peliculas = cleaned_data.get('peliculas')
    #     usuarios = cleaned_data.get('usuarios')
    #     if Transaccion.objects.filter(usuarios=usuarios, peliculas=peliculas).exists():
    #         raise ValidationError("Usted ya compro esta pelicula, no puede volver a comprarla")
    #     return self.cleaned_data

class UsuarioForm (forms.ModelForm):
    class Meta:
        # de que modelo crea el form
        model = Usuario
        # que campos muestra el form
        fields = ['nombre', 'email']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not all(part.isalpha() for part in nombre.split()):
            raise ValidationError('El nombre solo debe contener letras y espacios.')
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('El email ya está registrado.')
        return email