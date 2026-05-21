from django.contrib import admin
from .models import Autor, Genero, Libro, Usuario, Reserva


admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Reserva)