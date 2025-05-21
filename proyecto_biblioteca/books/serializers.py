from rest_framework import serializers
from .models import Libro, Autor, Resena

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'fecha_publicacion', 'resumen']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ['id', 'libro', 'texto', 'calificacion', 'fecha']
