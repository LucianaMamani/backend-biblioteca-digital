from django.urls import path, include


urlpatterns = [
    path('', include('libros.urls')),
    path('', include('reservas.urls')),
    path('', include('usuarios.urls')),
]