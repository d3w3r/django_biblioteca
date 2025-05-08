# Proyecto Biblioteca

Este proyecto sera una api construida con _[django][A1]_ para simular
los servicios utilizados en una biblioteca.

## Instalacion y Ejecucion desde consola

1. Descargar el codigo de la rama `main`.
2. Ingresa a la carpeta `proyecto_biblioteca` para la ejecucion de todos los comandos.
2. (opcional) Utiliza un entorno virtual:
   - Crear entorno virtual `python3 -m venv env`.
   - Activar entorno virtual `source env/bin/activate`.
3. Instala los paquetes requeridos `pip install -r requirements.txt`.
4. Corre las migraciones de la base de datos con el comando `python manage.py migrate`.
5. Crea un usuario para iniciar sesion con el comando `python manage.py createsuperuser`.
6. Finalmente ejecuta el servidor con el comando `python manage.py runserver`.

## Recursos externos

- Guia de faker [link][A2].
- Guia de queryset lookups de django [link][A3].
- Guia de query metodos de django [link][A4].
- Guia de aplicacion simple de django [link][A5].

[A1]: <https://www.djangoproject.com/>
[A2]: <https://faker.readthedocs.io/en/master/>
[A3]: <https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups>
[A4]: <https://docs.djangoproject.com/en/5.2/topics/db/queries/>
[A5]: <https://docs.djangoproject.com/en/5.2/intro/tutorial02/>
