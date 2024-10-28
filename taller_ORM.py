import os
import django
from datetime import date

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taller.settings')  # Cambia 'Taller' por el nombre de tu proyecto
django.setup()

from libreria.models import Libro, Autor  # Cambia 'libreria' por el nombre de tu aplicación

def main():
    # 1. Crear un nuevo registro en el modelo Libro
    Libro.objects.create(
        isbn="1234567890123",
        titulo="El Principito",
        paginas=98,
        fecha_publicacion=date(1943, 1, 1),
        estatus='A',
        categoria="Ficción",
        desc_corta="Un clásico de la literatura."
    )

    # 2. Crear un autor llamado "Antoine" y relacionarlo con el libro "El Principito"
    autor_antoine = Autor.objects.create(nombre="Antoine")
    libro_principito = Libro.objects.get(titulo="El Principito")
    libro_principito.autor.add(autor_antoine)

    # 3. Crear un libro con ISBN "9876543210987"
    Libro.objects.create(
        isbn="9876543210987",
        titulo="La Biblia",
        paginas=300,
        estatus='B',
        categoria="bíblicas"
    )

    # 4. Crear 4 autores y relacionarlos con los libros "El Principito" y "La Biblia"
    autores = [
        Autor(nombre="Autor 1"),
        Autor(nombre="Autor 2"),
        Autor(nombre="Autor 3"),
        Autor(nombre="Autor 4"),
    ]
    Autor.objects.bulk_create(autores)

    libro_principito = Libro.objects.get(titulo="El Principito")
    libro_biblia = Libro.objects.get(titulo="La Biblia")

    for autor in autores:
        libro_principito.autor.add(autor)
        libro_biblia.autor.add(autor)

    # 5. Obtener todos los libros cuya categoría sea "bíblicas" y tengan más de 100 páginas
    libros_biblia = Libro.objects.filter(categoria="bíblicas", paginas__gt=100)

    # 6. Mostrar todos los autores de "La Biblia"
    libro_biblia = Libro.objects.get(titulo="La Biblia")
    for autor in libro_biblia.libros_autores.all():
        print(autor.nombre)

    # 7. Obtener los libros publicados antes del año 2000 o que tengan más de 300 páginas
    from django.db.models import Q
    libros_publicados = Libro.objects.filter(Q(fecha_publicacion__lt=date(2000, 1, 1)) | Q(paginas__gt=300))

    # 8. Actualizar el número de páginas de un libro específico, duplicándolo
    libro_especifico = Libro.objects.get(isbn="1234567890123")
    libro_especifico.paginas *= 2
    libro_especifico.save()

    # 9. Incrementar el número de páginas en 10 para todos los libros que tengan más de 200 páginas
    libros_mas_200 = Libro.objects.filter(paginas__gt=200)
    for libro in libros_mas_200:
        libro.paginas += 10
        libro.save()

    # 10. Cambiar la categoría a "Educación" para todos los libros con estatus "C"
    Libro.objects.filter(estatus='C').update(categoria="Educación")

if __name__ == "__main__":
    main()
