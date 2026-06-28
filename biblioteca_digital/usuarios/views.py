from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer, RegisterSerializer


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
            return Response({
                'mensaje': 'Usuario creado correctamente',
                'id': user.id
            })

        return Response(serializer.errors, status=400)


@api_view(['GET'])
def me(request):
    auth = JWTAuthentication()

    try:
        result = auth.authenticate(request)

        if result is None:
            return Response({'detail': 'Token no encontrado'}, status=401)

        user, token = result

    except (InvalidToken, TokenError) as e:
        return Response({'detail': f'Token inválido: {str(e)}'}, status=401)

    reservas = user.reservas.filter(estado='activa').values(
        'id',
        'libro__titulo',
        'fecha_reserva',
        'fecha_devolucion',
        'estado'
    )

    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_staff': user.is_staff,
        'nombre': user.first_name or user.username,
        'apellido': user.last_name,
        'reservas': list(reservas),
    })