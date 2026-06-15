from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'autores',  views.AutorViewSet)
router.register(r'generos',  views.GeneroViewSet)
router.register(r'libros',   views.LibroViewSet)
router.register(r'reservas', views.ReservaViewSet, basename='reserva')
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'auth',     views.RegisterView,   basename='auth')

urlpatterns = [
    path('perfil/me/', views.me, name='usuario-me'),
    path('', include(router.urls)),
    path('usuarios/me/', views.me, name='me'),
]