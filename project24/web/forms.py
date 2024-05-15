from django import forms

class MedioDePagoForm(forms.Form):
    medios_de_pago = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('debito', 'Débito'),
        ('transferencia', 'Transferencia'),
    ]
    medios = forms.ChoiceField(choices=medios_de_pago, label='Medio de pago')