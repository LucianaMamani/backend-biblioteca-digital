# BiblioDigital

Sistema de biblioteca digital desarrollado como proyecto académico.
Permite explorar un catálogo de libros, realizar reservas y gestionar el inventario desde un panel de administración.

**Equipo:** Luciana Mamani · Mariano Abizanda  
**Año:** 2026

---

## Stack tecnológico

- **Backend:** Django 6.0.6 + Django REST Framework
- **Autenticación:** JWT (djangorestframework-simplejwt)
- **Base de datos:** SQLite
- **Frontend:** HTML5 + CSS3 + JavaScript vanilla

---

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/LucianaMamani/backend-biblioteca-digital.git
cd backend-biblioteca-digital
```

### 2. Instalar dependencias

```bash
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
```

### 3. Levantar el servidor

```bash
cd biblioteca_digital
python manage.py runserver
```

El servidor queda disponible en: http://127.0.0.1:8000

### 4. Crear un superusuario (administrador)

En una terminal separada (con el servidor corriendo):

```bash
cd biblioteca_digital
python manage.py createsuperuser
```

Seguir los pasos que aparecen en pantalla (nombre de usuario, email y contraseña).

### 5. Cargar datos de prueba

```bash
cd biblioteca_digital
python manage.py loaddata fixtures_libros.json
```

Esto carga autores, géneros y libros de ejemplo en la base de datos.

---

## URLs importantes

| URL | Descripción |
|-----|-------------|
| http://127.0.0.1:8000 | Página principal |
| http://127.0.0.1:8000/pages/login.html | Iniciar sesión |
| http://127.0.0.1:8000/pages/register.html | Registrarse |
| http://127.0.0.1:8000/pages/catalogo.html | Catálogo de libros |
| http://127.0.0.1:8000/pages/panel-usuario.html | Panel del usuario |
| http://127.0.0.1:8000/pages/panel-admin.html | Panel de administración |
| http://127.0.0.1:8000/admin/ | Panel de administración nativo de Django |
| http://127.0.0.1:8000/api/ | API REST |

---

## Endpoints de la API

| Método | URL | Descripción |
|--------|-----|-------------|
| GET/POST | /api/libros/ | Catálogo de libros |
| GET/POST | /api/autores/ | Autores |
| GET/POST | /api/generos/ | Géneros |
| GET/POST | /api/reservas/ | Reservas (requiere autenticación) |
| GET | /api/perfil/me/ | Datos del usuario autenticado |
| POST | /api/token/ | Obtener tokens JWT (login) |
| POST | /api/token/refresh/ | Renovar access token |
| POST | /api/auth/register/ | Registrar nuevo usuario |

---

## Roles de usuario

El sistema distingue dos tipos de usuarios:

- **Usuario normal:** se registra desde `/pages/register.html`. Puede explorar el catálogo, reservar libros y gestionar sus reservas desde su panel.
- **Administrador:** se crea con `python manage.py createsuperuser`. Tras loguearse, es redirigido automáticamente al panel de administración donde puede gestionar libros, autores, géneros, reservas y usuarios.

---

## Notas

- La base de datos (`db.sqlite3`) es local y no está incluida en el repositorio. Cada integrante del equipo mantiene la suya propia.
- Para compartir datos entre integrantes, usar el fixture: `python manage.py loaddata fixtures_libros.json`
- Para actualizar el fixture con datos nuevos, ejecutar: `python exportar.py` desde la carpeta `biblioteca_digital/`