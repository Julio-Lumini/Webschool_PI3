from django import forms
from .models import Material, Merenda, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'nome': 'Nome da Categoria',
            'descricao': 'Descrição da Categoria',
        }
    

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome_do_produto', 'fabricante', 'quantidade']
        widgets = {
            'nome_do_produto': forms.TextInput(attrs={'placeholder': 'Nome do Produto'}),
            'fabricante': forms.TextInput(attrs={'placeholder': 'Fabricante'}),
            'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
        }
        labels = {
            'nome_do_produto': 'Nome do Produto',
            'fabricante': 'Fabricante',
            'quantidade': 'Quantidade',
        }
        
        

class MerendaForm(forms.ModelForm):
    class Meta:
        model = Merenda
        fields = ['nome', 'quantidade', 'consumo']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade'}),
            'consumo': forms.NumberInput(attrs={'placeholder': 'Consumo'}),
        }
        labels = {
            'nome': 'Nome',
            'quantidade': 'Quantidade',
            'consumo': 'Consumo',
        }
class ImportMerendaForm(forms.Form):
    arquivo = forms.FileField(label='Arquivo Excel')
    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        if not arquivo.name.endswith('.xlsx'):
            raise forms.ValidationError('O arquivo deve ser um arquivo Excel (.xlsx)')
        return arquivo
class ExportMerendaForm(forms.Form):
    exportar = forms.BooleanField(required=False, label='Exportar Merenda')
