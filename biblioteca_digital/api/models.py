from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    anio_publicacion = models.IntegerField()
    disponibilidad = models.CharField(max_length=50)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    fecha_reserva = models.DateField()
    estado = models.CharField(max_length=50)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.libro}"