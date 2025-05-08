from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Plan
        fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'capacidad_maxima']