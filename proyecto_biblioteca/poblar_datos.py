from faker import Faker
# from books.models import Autor, Libro, Resena

faker = Faker()

def generate_autor():
    autor = {
        "nombre": faker.name(),
        "nacionalidad": faker.country(),
    }
    return autor

def generate_libro(id_autor):
    libro = {
        "titulo": faker.sentence(nb_words=4),
        "autor": id_autor,
        "fecha_publicacion": faker.date(),
        "resumen": faker.text(),
    }
    return libro

def generate_resena(id_libro):
    resena = {
        "libro": id_libro,
        "texto": faker.text(),
        "calificacion": faker.random_int(min=0, max=5),
        "fecha": faker.date(),
    }
    return resena

# print(generate_autor())
# print(generate_libro(faker.random_digit()))
# print(generate_resena(1))
