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
6. Carga la base de datos ejecutando el comando `python manage.py shell < poblar_datos.py`.
7. Finalmente ejecuta el servidor con el comando `python manage.py runserver`.

## Capturas de pantalla

![image](https://github.com/user-attachments/assets/3a168024-8674-41c6-9da1-331403bc9236)
_Panel admin con Autores_

![image](https://github.com/user-attachments/assets/c46ce9e8-2374-4344-99fe-cd595c17c1ad)
_Panel admin con Libros_

![image](https://github.com/user-attachments/assets/7170285f-a88f-4c94-bc24-141b22c16afc)
_Panel admin con Resenas_

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
