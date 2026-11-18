# API Hola Mundo con Django

## Descripción
Este proyecto consiste en la creación de una API REST utilizando Python y Django. Su objetivo es desarrollar un servicio web sencillo que responda a una solicitud HTTP GET y devuelva un mensaje en formato JSON.

## Tecnologías utilizadas
- Python 3.14
- Django 6.1
- Visual Studio Code
- Postman
- Git y GitHub

## Endpoint

**Método:** GET

**Ruta:** `/api/hola`

**URL local:** `http://127.0.0.1:8000/api/hola`

## Respuesta JSON

```json
{
  "mensaje": "Hola Mundo",
  "lenguaje": "Python",
  "framework": "Django"
}
```

## Instalación y ejecución

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar Django.
4. Ejecutar el servidor de desarrollo.

```bash
pip install django
python manage.py runserver
```

## Autor
Proyecto académico desarrollado como práctica de creación de una API REST con Python y Django.
