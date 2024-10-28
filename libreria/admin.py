from django.contrib import admin
from .models import Editorial, Libro, LibroCronica, Autor, AutorCapitulo

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo', 'paginas', 'fecha_publicacion', 'estatus', 'editorial')
    search_fields = ('titulo', 'isbn')
    list_filter = ('estatus', 'editorial')

@admin.register(LibroCronica)
class LibroCronicaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'descripcion_larga')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(AutorCapitulo)
class AutorCapituloAdmin(admin.ModelAdmin):
    list_display = ('autor', 'libro', 'numero_capitulos')
