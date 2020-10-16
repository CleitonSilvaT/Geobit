from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Autor
from .forms import LivroForm, AutorForm
# Create your views here.


def livros_list(request):
    template_name = 'livros/livros_list.html'
    livros = Livro.objects.all()
    context = {'livros':livros}
    return render(request, template_name, context)

def livros_delete(request, id=None):
    template_name = 'livros/livros_delete.html'
    livro = get_object_or_404(Livro, id=id)
    context = {'livro':livro}

    if request.method == 'POST':
        livro.delete()
        return redirect('livros_list')

    return render(request, template_name, context)

def livros_add(request):
    template_name = 'livros/livros_add.html'
    form = LivroForm(request.POST)
    context = {'form':form}

    if form.is_valid():
        obj = form.save()
        obj.save()
        form = LivroForm()
        return redirect('livros_list')

    return render(request, template_name, context)

def livros_edit(request, id):
    template_name = 'livros/livros_edit.html'
    livro = get_object_or_404(Livro, id=id)
    form = LivroForm(request.POST or None, instance=livro)
    context = {'form':form}

    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('livros_list')

    return render(request, template_name, context)


def autor_list(request):
    template_name = 'livros/autor_list.html'
    autores = Autor.objects.all()
    context = {'autores':autores}
    return render(request, template_name, context)

def autor_delete(request, id=None):
    template_name = 'livros/autor_delete.html'
    autor = get_object_or_404(Autor, id=id)
    context = {'autor':autor}

    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')

    return render(request, template_name, context)

def autor_add(request):
    template_name = 'livros/autor_add.html'
    form = AutorForm(request.POST)
    context = {'form':form}

    if form.is_valid():
        obj = form.save()
        obj.save()
        form = AutorForm()
        return redirect('autor_list')

    return render(request, template_name, context)

def autor_edit(request, id):
    template_name = 'livros/autor_edit.html'
    autor = get_object_or_404(Autor, id=id)
    form = AutorForm(request.POST or None, instance=autor)
    context = {'form':form}

    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('autor_list')

    return render(request, template_name, context)