from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import os
from django.conf import settings

def home(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('{% load static %}', '').replace(
        "{% static 'img/books-hero3.jpg' %}", '/static/img/books-hero3.jpg'
    )
    return HttpResponse(content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home, name='home'),
]