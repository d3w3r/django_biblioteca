# Proyecto Biblioteca

Este proyecto sera una api construida con _[django][A1]_ para simular
los servicios utilizados en una biblioteca.

## Instalacion

1. Descargar el codigo de la rama `main`.
2. (opcional) Utiliza un entorno virtual:
   - Crear entorno virtual `python3 -m venv env`.
   - Activar entorno virtual `source env/bin/activate`.
3. Instala los paquetes requeridos `pip install -r requirements.txt`.
4. Instala las dependencias:
   1. `pip install --upgrade pip`.
   2. `pip install django`.
5. Corre las migraciones de la base de datos con el comando `python manage.py migrate`.
6. Crea un usuario para iniciar sesion con el comando `python manage.py createsuperuser`.
5. Finalmente ejecuta el servidor con el comando `python manage.py runserver`.

[A1]: <https://www.djangoproject.com/>
