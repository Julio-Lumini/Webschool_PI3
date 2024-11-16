from django import forms
from .models import Material, Merenda

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'quantidade']

class MerendaForm(forms.ModelForm):
    class Meta:
        model = Merenda
        fields = ['nome', 'quantidade' ]
