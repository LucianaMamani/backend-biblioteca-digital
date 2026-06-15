from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, Http404
import os
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import FileResponse
import mimetypes

def home(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('{% load static %}', '').replace(
        "{% static 'img/books-hero3.jpg' %}", '/static/img/books-hero3.jpg'
    )
    return HttpResponse(content)

def pagina(request, nombre):
    page_path = os.path.join(settings.BASE_DIR, '..', 'pages', nombre)
    if not os.path.exists(page_path):
        raise Http404(f'Página {nombre} no encontrada')
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return HttpResponse(content)

def archivo_estatico(request, carpeta, nombre):
    file_path = os.path.join(settings.BASE_DIR, '..', carpeta, nombre)
    if not os.path.exists(file_path):
        raise Http404()
    mime_type, _ = mimetypes.guess_type(file_path)
    return FileResponse(open(file_path, 'rb'), content_type=mime_type or 'text/plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pages/<str:nombre>', pagina, name='pagina'),
    path('<str:carpeta>/<str:nombre>', archivo_estatico, name='estatico'),
    path('', home, name='home'),
]

