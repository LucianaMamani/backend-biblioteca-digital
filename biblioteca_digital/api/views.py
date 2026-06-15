from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Autor, Genero, Libro, Reserva
from .serializers import (
    AutorSerializer, GeneroSerializer, LibroSerializer,
    ReservaSerializer, UsuarioSerializer, RegisterSerializer
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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
    
@api_view(['GET'])
def me(request):
    from rest_framework_simplejwt.authentication import JWTAuthentication
    from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
    
    auth = JWTAuthentication()
    try:
        result = auth.authenticate(request)
        if result is None:
            return Response({'detail': 'Token no encontrado'}, status=401)
        user, token = result
    except (InvalidToken, TokenError) as e:
        return Response({'detail': f'Token inválido: {str(e)}'}, status=401)

    reservas = user.reservas.filter(estado='activa').values(
        'id', 'libro__titulo', 'fecha_reserva', 'fecha_devolucion', 'estado'
    )
    return Response({
        'id':       user.id,
        'username': user.username,
        'email':    user.email,
        'nombre':   user.first_name or user.username,
        'apellido': user.last_name,
        'reservas': list(reservas),
    })