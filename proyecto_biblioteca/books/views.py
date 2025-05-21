from rest_framework import viewsets
from .models import Libro, Autor, Resena
from .serializers import LibroSerializer, AutorSerializer, ResenaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all().order_by('-fecha')
    serializer_class = ResenaSerializer

