from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'generos', views.GeneroViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]