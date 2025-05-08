from django.contrib import admin
from .models import Libro, Autor, Resena

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', "numero_libros",)
    search_fields = ('nacionalidad', 'nombre')

    def numero_libros(self, obj):
        return obj.libros.count()

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'resumen', "numero_resenas")
    search_fields = ('autor',)
    list_filter = ('autor',)

    def numero_resenas(self, obj):
        return obj.resenas.count()

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'texto', 'calificacion', 'fecha')
    search_fields = ('texto', 'calificacion')
    list_filter = ('libro',)
