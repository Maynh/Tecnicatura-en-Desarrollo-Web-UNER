from modulos_comunes.modules_generales import abrir_archivo, guardar_datos, generar_id

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
    guardar_datos(RUTA_LIBROS, libros)
    print(f'\U0001F4D6 Libro "{titulo}" registrado con éxito.')

def editar_libro(id_libro):
    libros = abrir_archivo(RUTA_LIBROS)
    for libro in libros:
        if libro['id'] == id_libro:
            print(f"Datos actuales del libro con ID {id_libro}:")
            print(libro)  # Mostrar datos actuales como diccionario
            while True:
                print("\nOpciones de edición:")
                print("1. \U0001F4D6 Título")
                print("2. \U0001F4D8 Autor")
                print("3. \U0001F4DA Editorial")
                print("4. \U0001F4C5 Año de Publicación")
                print("5. \U0001F4D1 Género")
                print("6. \U0001F4D2 Cantidad Disponible")
                print("0. \U0001F6AA Salir")
                opcion = input("Seleccione una opción para editar: ")

                if opcion == "1":
                    nuevo_valor = input("Ingrese el nuevo título: ")
                    libro['titulo'] = nuevo_valor
                elif opcion == "2":
                    nuevo_valor = input("Ingrese el nuevo autor: ")
                    libro['autor'] = nuevo_valor
                elif opcion == "3":
                    nuevo_valor = input("Ingrese la nueva editorial: ")
                    libro['editorial'] = nuevo_valor
                elif opcion == "4":
                    nuevo_valor = input("Ingrese el nuevo año de publicación: ")
                    libro['anio_publicacion'] = nuevo_valor
                elif opcion == "5":
                    nuevo_valor = input("Ingrese el nuevo género: ")
                    libro['genero'] = nuevo_valor
                elif opcion == "6":
                    nuevo_valor = input("Ingrese la nueva cantidad disponible: ")
                    libro['cantidad_disponible'] = nuevo_valor
                elif opcion == "0":
                    break
                else:
                    print("\U000026A0\U0000FE0F Opción no válida.")
                    continue

                guardar_datos(RUTA_LIBROS, libros)
                print(f'\U0001F4D6 Libro con ID {id_libro} editado con éxito.')
            return
    print(f'\U0001F6AB Libro con ID {id_libro} no encontrado.')

def eliminar_libro(id_libro):
    libros = abrir_archivo(RUTA_LIBROS)
    libro_encontrado = None

    for libro in libros:
        if libro['id'] == id_libro:
            libro_encontrado = libro
            break

    if libro_encontrado:
        libros.remove(libro_encontrado)
        guardar_datos(RUTA_LIBROS, libros)
        print(f'\U0001F5D1 Libro "{libro_encontrado["titulo"]}" con ID {id_libro} eliminado con éxito.')
    else:
        print(f'\U0001F6AB Libro con ID {id_libro} no encontrado.')

def buscar_libro_por_id(id_libro):
    libros = abrir_archivo(RUTA_LIBROS)
    for libro in libros:
        if libro['id'] == id_libro:
            print(libro)
            return
    print(f'\U0001F50D Libro con ID {id_libro} no encontrado.')








