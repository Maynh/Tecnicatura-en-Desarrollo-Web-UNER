from modulos_comunes.modules_generales import abrir_archivo, escribir_archivo, generar_id

RUTA_LIBROS = 'datos/libros.json'

def registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
    libros = abrir_archivo(RUTA_LIBROS)
    nuevo_libro = {
        'id': generar_id(RUTA_LIBROS),
        'titulo': titulo,
        'autor': autor,
        'editorial': editorial,
        'anio_publicacion': anio_publicacion,
        'genero': genero,
        'cantidad_disponible': cantidad_disponible
    }
    libros.append(nuevo_libro)
    escribir_archivo(RUTA_LIBROS, libros)
    print(f'Libro "{titulo}" registrado con éxito.')

def editar_libro(id_libro, titulo=None, autor=None, editorial=None, anio_publicacion=None, genero=None, cantidad_disponible=None):
    libros = abrir_archivo(RUTA_LIBROS)
    for libro in libros:
        if libro['id'] == id_libro:
            if titulo: libro['titulo'] = titulo
            if autor: libro['autor'] = autor
            if editorial: libro['editorial'] = editorial
            if anio_publicacion: libro['anio_publicacion'] = anio_publicacion
            if genero: libro['genero'] = genero
            if cantidad_disponible: libro['cantidad_disponible'] = cantidad_disponible
            escribir_archivo(RUTA_LIBROS, libros)
            print(f'Libro con ID {id_libro} editado con éxito.')
            return
    print(f'Libro con ID {id_libro} no encontrado.')

def eliminar_libro(id_libro):
    libros = abrir_archivo(RUTA_LIBROS)
    libros = [libro for libro in libros if libro['id'] != id_libro]
    escribir_archivo(RUTA_LIBROS, libros)
    print(f'Libro con ID {id_libro} eliminado con éxito.')

def buscar_libro(campo, valor):
    libros = abrir_archivo(RUTA_LIBROS)
    resultados = [libro for libro in libros if libro[campo] == valor]
    for libro in resultados:
        print(libro)

