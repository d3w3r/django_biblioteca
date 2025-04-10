from django.contrib import admin
from .models import Libro, Autor, Resena

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', "book_count")
    search_fields = ('nacionalidad', 'nombre')

    def book_count(self, obj):
        return obj.libros.count()

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'resumen')
    search_fields = ('autor',)
    list_filter = ('autor',)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'texto', 'calificacion', 'fecha')