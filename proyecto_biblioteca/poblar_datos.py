import random
from faker import Faker
from books.models import Autor, Libro, Resena

faker = Faker()

def generate_autor():
    autor = {
        "nombre": faker.name(),
        "nacionalidad": faker.country(),
    }
    return autor

def generate_libro(autor):
    libro = {
        "titulo": faker.sentence(nb_words=4),
        "autor": autor,
        "fecha_publicacion": faker.date(),
        "resumen": faker.text(),
    }
    return libro

def generate_resena(libro):
    resena = {
        "libro": libro,
        "texto": faker.text(),
        "calificacion": random.randint(0, 5),
        "fecha": faker.date(),
    }
    return resena

def imp_load():
    total_de_autores = random.randint(5, 10)
    total_de_libros = random.randint(10, 20)
    total_de_resenas = random.randint(20, 25)

    for x in range(total_de_autores):
        created = generate_autor()
        autor = Autor.objects.create(
            nombre=created['nombre'],
            nacionalidad=created['nacionalidad'],
        )
    autores = Autor.objects.all()

    for x in range(total_de_libros):
        selected_autor = random.choice(autores)

        created = generate_libro(selected_autor)
        libro = Libro.objects.create(
            autor=created['autor'],
            titulo=created['titulo'],
            resumen=created['resumen'],
            fecha_publicacion=created['fecha_publicacion'],
        )
    libros = Libro.objects.all()

    for x in range(total_de_resenas):
        selected_libro = random.choice(libros)

        created = generate_resena(selected_libro)
        resena = Resena.objects.create(
            libro=created['libro'],
            texto=created['texto'],
            fecha=created['fecha'],
            calificacion=created['calificacion'],
        )

imp_load()
