from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Autor, Genero, Libro, Reserva

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Autor
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Genero
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor_nombre  = serializers.CharField(source='autor.nombre', read_only=True)
    genero_nombre = serializers.CharField(source='genero.nombre', read_only=True)

    class Meta:
        model  = Libro
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    libro_titulo   = serializers.CharField(source='libro.titulo', read_only=True)

    class Meta:
        model  = Reserva
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model  = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username   = validated_data['username'],
            email      = validated_data.get('email', ''),
            password   = validated_data['password'],
            first_name = validated_data.get('first_name', ''),
            last_name  = validated_data.get('last_name', ''),
        )
        return user