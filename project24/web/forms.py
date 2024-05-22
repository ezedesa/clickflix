from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario', required=True)
    clave = forms.CharField(label='Contraseña', required=True)

class MedioDePagoForm(forms.Form):
    medios_de_pago = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('debito', 'Débito'),
        ('transferencia', 'Transferencia'),
    ]
    nombre = forms.CharField(label="Nombre", required=True) 
    apellido = forms.CharField(label="Apellido", required=True) 
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