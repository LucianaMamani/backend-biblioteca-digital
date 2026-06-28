from django.contrib import admin
from api.models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'libro', 'fecha_reserva', 'fecha_devolucion', 'estado')
    list_filter = ('estado',)
    search_fields = ('usuario__username', 'libro__titulo')