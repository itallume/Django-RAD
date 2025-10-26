from django import forms
from .models import Editora, Livro, Autor, Publica


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['isbn', 'titulo', 'data_publicacao', 'preco', 'estoque', 'editora']
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
        }


class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        fields = ['livro', 'autor']
        widgets = {
            'livro': forms.Select(attrs={'class': 'form-select'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }
