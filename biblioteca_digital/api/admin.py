from django.contrib import admin
from .models import Autor, Genero, Libro, Reserva

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display  = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display   = ('titulo', 'autor', 'genero', 'anio', 'disponible')
    list_filter    = ('disponible', 'genero')
    search_fields  = ('titulo', 'autor__nombre')
    list_editable  = ('disponible',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display  = ('usuario', 'libro', 'fecha_reserva', 'fecha_devolucion', 'estado')
    list_filter   = ('estado',)
    search_fields = ('usuario__username', 'libro__titulo')

# Register your models here.
