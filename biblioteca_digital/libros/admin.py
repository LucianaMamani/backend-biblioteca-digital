from django.contrib import admin
from api.models import Autor, Genero, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'anio', 'disponible')
    list_filter = ('disponible', 'genero')
    search_fields = ('titulo', 'autor__nombre')
    list_editable = ('disponible',)