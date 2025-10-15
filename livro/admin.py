from django.contrib import admin
from .models import Editora, Livro, Autor, Publica

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'isbn', 'editora', 'preco', 'estoque')
    list_filter = ('editora', 'data_publicacao')
    search_fields = ('titulo', 'isbn')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
    list_display = ('livro', 'autor')
    list_filter = ('livro', 'autor')
    search_fields = ('livro__titulo', 'autor__nome')
