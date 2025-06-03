from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['ruc', 'dv','nombre', 'contabilidad', 'estado', 'fdesde', 'fhasta']
        widgets = {
            'fdesde': forms.DateInput(attrs={'type': 'date'}),
            'fhasta': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get('estado')

        if estado == 'SUSPENSION TEMPORAL':
            fecha_suspension = cleaned_data.get('fdesde')
            fecha_reinicio = cleaned_data.get('fhasta')

            if not fecha_suspension or not fecha_reinicio:
                raise forms.ValidationError("Debe completar las fechas de suspensión y reinicio.")


