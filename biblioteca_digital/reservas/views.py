from rest_framework import viewsets, permissions
from api.models import Reserva
from .serializers import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Reserva.objects.all()

        return Reserva.objects.filter(usuario=user)

    def perform_create(self, serializer):
        libro = serializer.validated_data['libro']
        libro.disponible = False
        libro.save()
        serializer.save(usuario=self.request.user)

    def perform_destroy(self, instance):
        instance.libro.disponible = True
        instance.libro.save()
        instance.delete()