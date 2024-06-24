from modulos_comunes.modules_generales import abrir_archivo, guardar_datos, generar_id

RUTA_SOCIOS = 'datos/socios.json'

def registrar_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono):
    socios = abrir_archivo(RUTA_SOCIOS)
    nuevo_socio = {
        'id': generar_id(RUTA_SOCIOS),
        'nombre': nombre,
        'apellido': apellido,
        'fecha_nacimiento': fecha_nacimiento,
        'direccion': direccion,
        'correo_electronico': correo_electronico,
        'telefono': telefono
    }
    socios.append(nuevo_socio)
    guardar_datos(RUTA_SOCIOS, socios)
    print(f'\U0001F9D1\U0000200D\U0001F4BC Socio "{nombre} {apellido}" registrado con éxito.')

def editar_socio(id_socio):
    socios = abrir_archivo(RUTA_SOCIOS)
    for socio in socios:
        if socio['id'] == id_socio:
            print(f"Datos actuales del socio con ID {id_socio}:")
            print(socio)  # Mostrar datos actuales como diccionario
            while True:
                print("\nOpciones de edición:")
                print("1. \U0001F464 Nombre")
                print("2. \U0001F465 Apellido")
                print("3. \U0001F4C5 Fecha de Nacimiento")
                print("4. \U0001F3E0 Dirección")
                print("5. \U0001F4E7 Correo Electrónico")
                print("6. \U0001F4DE Teléfono")
                print("0. \U0001F6AA Salir")
                opcion = input("Seleccione una opción para editar: ")

                if opcion == "1":
                    nuevo_valor = input("Ingrese el nuevo nombre: ")
                    socio['nombre'] = nuevo_valor
                elif opcion == "2":
                    nuevo_valor = input("Ingrese el nuevo apellido: ")
                    socio['apellido'] = nuevo_valor
                elif opcion == "3":
                    nuevo_valor = input("Ingrese la nueva fecha de nacimiento: ")
                    socio['fecha_nacimiento'] = nuevo_valor
                elif opcion == "4":
                    nuevo_valor = input("Ingrese la nueva dirección: ")
                    socio['direccion'] = nuevo_valor
                elif opcion == "5":
                    nuevo_valor = input("Ingrese el nuevo correo electrónico: ")
                    socio['correo_electronico'] = nuevo_valor
                elif opcion == "6":
                    nuevo_valor = input("Ingrese el nuevo teléfono: ")
                    socio['telefono'] = nuevo_valor
                elif opcion == "0":
                    break
                else:
                    print("\U000026A0\U0000FE0F Opción no válida.")
                    continue

                guardar_datos(RUTA_SOCIOS, socios)
                print(f'\U0001F9D1\U0000200D\U0001F4BC Socio con ID {id_socio} editado con éxito.')
            return
    print(f'\U0001F6AB Socio con ID {id_socio} no encontrado.')

def eliminar_socio(id_socio):
    socios = abrir_archivo(RUTA_SOCIOS)
    socio_encontrado = None

    for socio in socios:
        if socio['id'] == id_socio:
            socio_encontrado = socio
            break

    if socio_encontrado:
        socios.remove(socio_encontrado)
        guardar_datos(RUTA_SOCIOS, socios)
        print(f'\U0001F5D1 Socio "{socio_encontrado["nombre"]} {socio_encontrado["apellido"]}" con ID {id_socio} eliminado con éxito.')
    else:
        print(f'\U0001F6AB Socio con ID {id_socio} no encontrado.')

def buscar_socio():
    socios = abrir_archivo(RUTA_SOCIOS)
    print("\U0001F50D Opciones de búsqueda:")
    print("1. \U0001F194 Buscar por ID")
    print("2. \U0001F4D1 Buscar por DNI")
    try:
        opcion = int(input("\U0001F449 Seleccione una opción de búsqueda: "))
    except ValueError:
        print("\U000026A0\U0000FE0F Error: Por favor, ingrese un número válido.")
        return

    if opcion == 1:
        try:
            id_socio = int(input("\U0001F194 Ingrese el ID del socio: "))
        except ValueError:
            print("\U000026A0\U0000FE0F Error: Por favor, ingrese un número válido.")
            return
        for socio in socios:
            if socio['id'] == id_socio:
                print(socio)
                return
        print(f'\U0001F6AB Socio con ID {id_socio} no encontrado.')

    elif opcion == 2:
        dni = input("\U0001F4D1 Ingrese el DNI del socio: ")
        for socio in socios:
            if socio['dni'] == dni:
                print(socio)
                return
        print(f'\U0001F6AB Socio con DNI {dni} no encontrado.')

    else:
        print("\U0001F6AB Opción no válida.")







