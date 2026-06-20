import os
import django
import io
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_digital.settings')
django.setup()

from django.core.management import call_command

with io.open('fixtures_libros.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'api.Autor', 'api.Genero', 'api.Libro', indent=2, stdout=f)

print("Listo")