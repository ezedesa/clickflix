from django import forms
from django.core.exceptions import ValidationError

from .models import Pelicula

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario')
    clave = forms.CharField(label='Contraseña')

class MedioDePagoForm(forms.Form):
    medios_de_pago = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('debito', 'Débito'),
        ('transferencia', 'Transferencia'),
    ]
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido") 
    numero_tarjeta = forms.IntegerField(label="Número de tarjeta")
    medios = forms.ChoiceField(choices=medios_de_pago, label='Medio de pago')

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")
        return self.cleaned_data["nombre"]
        
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")
        return self.cleaned_data["apellido"]

    def clean(self):

        if self.cleaned_data["numero_tarjeta"] < 1000000000000000:
            raise ValidationError("El número de tarjeta debe tener 16 dígitos")

        return self.cleaned_data
    

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