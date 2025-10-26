from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Editora, Livro, Autor, Publica
from .forms import EditoraForm, LivroForm, AutorForm, PublicaForm


# Editora
class EditoraListView(ListView):
    model = Editora
    template_name = 'livro/editora_list.html'
    context_object_name = 'editoras'


class EditoraDetailView(DetailView):
    model = Editora
    template_name = 'livro/editora_detail.html'


class EditoraCreateView(CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'livro/editora_form.html'
    success_url = reverse_lazy('livro:editora-list')


class EditoraUpdateView(UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'livro/editora_form.html'
    success_url = reverse_lazy('livro:editora-list')


class EditoraDeleteView(DeleteView):
    model = Editora
    template_name = 'livro/editora_confirm_delete.html'
    success_url = reverse_lazy('livro:editora-list')


# Autor
class AutorListView(ListView):
    model = Autor
    template_name = 'livro/autor_list.html'
    context_object_name = 'autores'


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'livro/autor_detail.html'


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'livro/autor_form.html'
    success_url = reverse_lazy('livro:autor-list')


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'livro/autor_form.html'
    success_url = reverse_lazy('livro:autor-list')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'livro/autor_confirm_delete.html'
    success_url = reverse_lazy('livro:autor-list')


# Livro
class LivroListView(ListView):
    model = Livro
    template_name = 'livro/livro_list.html'
    context_object_name = 'livros'


class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livro/livro_detail.html'


class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro/livro_form.html'
    success_url = reverse_lazy('livro:livro-list')


class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro/livro_form.html'
    success_url = reverse_lazy('livro:livro-list')


class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livro/livro_confirm_delete.html'
    success_url = reverse_lazy('livro:livro-list')


# Publica
class PublicaListView(ListView):
    model = Publica
    template_name = 'livro/publica_list.html'
    context_object_name = 'publicacoes'


class PublicaDetailView(DetailView):
    model = Publica
    template_name = 'livro/publica_detail.html'


class PublicaCreateView(CreateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'livro/publica_form.html'
    success_url = reverse_lazy('livro:publica-list')


class PublicaUpdateView(UpdateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'livro/publica_form.html'
    success_url = reverse_lazy('livro:publica-list')


class PublicaDeleteView(DeleteView):
    model = Publica
    template_name = 'livro/publica_confirm_delete.html'
    success_url = reverse_lazy('livro:publica-list')
from django.shortcuts import render

# Create your views here.
