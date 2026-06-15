from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Autor, Genero, Libro, Reserva
from .serializers import (
    AutorSerializer, GeneroSerializer, LibroSerializer,
    ReservaSerializer, UsuarioSerializer, RegisterSerializer
)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Libro.objects.all()
        genero   = self.request.query_params.get('genero')
        autor    = self.request.query_params.get('autor')
        buscar   = self.request.query_params.get('buscar')
        disponible = self.request.query_params.get('disponible')
        if genero:
            queryset = queryset.filter(genero__id=genero)
        if autor:
            queryset = queryset.filter(autor__id=autor)
        if buscar:
            queryset = queryset.filter(titulo__icontains=buscar)
        if disponible is not None:
            queryset = queryset.filter(disponible=disponible == 'true')
        return queryset

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

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]

class RegisterView(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'mensaje': 'Usuario creado correctamente', 'id': user.id})
        return Response(serializer.errors, status=400)