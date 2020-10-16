from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class PositiveIntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(PositiveIntegerRangeField, self).formfield(**defaults)

class Livro(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    quantidade_paginas = PositiveIntegerRangeField('Quantidade de Páginas', min_value=1, default=1)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    data_inclusao = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    