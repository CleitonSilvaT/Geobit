from django.urls import path
from .views import livros_list, livros_delete, livros_add, livros_edit
from .views import autor_list, autor_delete, autor_add, autor_edit

urlpatterns = [
    path('', livros_list, name='livros_list'),
    path('livros_list/', livros_list, name='livros_list'),
    path('livros_delete/<int:id>', livros_delete),
    path('livros_edit/<int:id>', livros_edit),
    path('livros_add/', livros_add, name='livros_add'),
    path('autor_list/', autor_list, name='autor_list'),
    path('autor_delete/<int:id>', autor_delete),
    path('autor_edit/<int:id>', autor_edit),
    path('autor_add/', autor_add, name='autor_add')
]
