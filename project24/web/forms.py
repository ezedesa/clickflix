from django import forms
from django.core.exceptions import ValidationError

class MedioDePagoForm(forms.Form):
    medios_de_pago = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('debito', 'Débito'),
        ('transferencia', 'Transferencia'),
    ]
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'})) 
    apellido = forms.CharField(label="Apellido", required=True) 
    dni = forms.IntegerField(label="DNI", required=True)
    medios = forms.ChoiceField(choices=medios_de_pago, label='Medio de pago')

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")
        return self.cleaned_data["nombre"]
        
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")
    def clean(self):
        cleaned_data = super().clean()
        #nombre = cleaned_data.get("nombre")
        #apellido = cleaned_data.get("apellido")
        
        #if nombre == "Carlos" and apellido == "Lopez":
         #   raise ValidationError("El usuario Carlos Lopez ya existe")
        
        if self.cleaned_data["dni"] < 10000000:
            raise ValidationError("El dni debe tener 8 digitos")

        return self.cleaned_data