from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre       = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=100, blank=True)
    bio          = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Autores'


class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Géneros'


class Libro(models.Model):
    titulo      = models.CharField(max_length=300)
    autor       = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    genero      = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, related_name='libros')
    anio        = models.IntegerField(null=True, blank=True)
    isbn        = models.CharField(max_length=20, blank=True)
    descripcion = models.TextField(blank=True)
    disponible  = models.BooleanField(default=True)
    portada     = models.CharField(max_length=10, default='📖')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Libros'


class Reserva(models.Model):
    ESTADOS = [
        ('activa',   'Activa'),
        ('vencida',  'Vencida'),
        ('cancelada','Cancelada'),
    ]
    usuario          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    libro            = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva    = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    estado           = models.CharField(max_length=10, choices=ESTADOS, default='activa')

    def __str__(self):
        return f'{self.usuario} - {self.libro} ({self.estado})'

    class Meta:
        verbose_name_plural = 'Reservas'
