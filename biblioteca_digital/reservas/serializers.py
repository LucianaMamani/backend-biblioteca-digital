from rest_framework import serializers
from api.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    libro_titulo = serializers.CharField(source='libro.titulo', read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ('usuario', 'fecha_reserva', 'estado')