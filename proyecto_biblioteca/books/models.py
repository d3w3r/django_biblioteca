from django.db import models
from datetime import timedelta
from django.utils import timezone

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField()

    def was_published_recently(self):
        return self.fecha_publicacion >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        return self.fecha >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"
