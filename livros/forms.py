from django import forms
from .models import Livro, Autor

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'quantidade_paginas', 'preco']
        widget = {
            'nome': forms.TextInput(attrs={'placeholder':'Informe o nome do livro'}),
            'autor': forms.TextInput(attrs={'placeholder':'Informe o nome do autor'}),
            'quantidade_paginas': forms.TextInput(attrs={'placeholder':'Informe a quantidade de páginas'}),
            'preco': forms.Textarea(attrs={'placeholder':'Informe o preço'})
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'