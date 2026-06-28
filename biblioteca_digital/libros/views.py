from rest_framework import viewsets, permissions
from api.models import Autor, Genero, Libro
from .serializers import AutorSerializer, GeneroSerializer, LibroSerializer


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
        genero = self.request.query_params.get('genero')
        autor = self.request.query_params.get('autor')
        buscar = self.request.query_params.get('buscar')
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