from rest_framework import serializers
from api.models import Autor, Genero, Libro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.nombre', read_only=True)
    genero_nombre = serializers.CharField(source='genero.nombre', read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'