from modulos_gestion.libros import registrar_libro, editar_libro, eliminar_libro, buscar_libro
from modulos_gestion.socios import registrar_socio, editar_socio, eliminar_socio, buscar_socio
from modulos_gestion.prestamos import registrar_prestamo, registrar_devolucion, generar_reporte_por_socio, generar_reporte_por_libro, generar_reporte_por_fecha

def menu():
    print("********* \U0001F4DA Bienvenido al Sistema de Gestión de Bibliotecas \U0001F4DA *********")
    print(" \U0001F60A ***Seleccione una opción para progresar con la gestión de la biblioteca*** \U0001F60A: ")

    print('1: \U0001F4D6 Registrar Libro')  # 📚
    print('2: \U0001F9D1\U0000200D\U0001F4BC Registrar Socio')  # 🧑‍💼
    print('3: \U0001F4D2 Registrar Préstamo')  # 📖
    print('4: \U0001F504 Registrar Devolución')  # 🔄
    print('5: \U0000270F\U0000FE0F Editar Libro')  # ✏️
    print('6: \U0001F4DD Editar Socio')  # 📝
    print('7: \U0000274C Eliminar Libro')  # ❌
    print('8: \U0001F5D1\U0000FE0F Eliminar Socio')  # 🗑️
    print('9: \U0001F50D Buscar Libro')  # 🔍
    print('10: \U0001F50D Buscar Socio')  # 🔍
    print('11: \U0001F4CA Generar Reporte de Préstamos por Socio')  # 📊
    print('12: \U0001F4CA Generar Reporte de Préstamos por Libro')  # 📊
    print('13: \U0001F4CA Generar Reporte de Préstamos por Fecha')  # 📊
    print('0: \U0001F6AA Salir')  # 🚪
    return int(input('Seleccione una opción: '))

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            titulo = input('Título: ')
            autor = input('Autor: ')
            editorial = input('Editorial: ')
            anio_publicacion = input('Año de Publicación: ')
            genero = input('Género: ')
            cantidad_disponible = int(input('Cantidad Disponible: '))
            registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible)
        elif opcion == 2:
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            fecha_nacimiento = input('Fecha de Nacimiento: ')
            direccion = input('Dirección: ')
            correo_electronico = input('Correo Electrónico: ')
            telefono = input('Teléfono: ')
            registrar_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono)
        elif opcion == 3:
            id_socio = int(input('ID de Socio: '))
            id_libro = int(input('ID de Libro: '))
            fecha_prestamo = input('Fecha de Préstamo: ')
            costo = input('Costo (opcional): ')
            registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo)
        elif opcion == 4:
            id_prestamo = int(input('ID de Préstamo: '))
            fecha_devolucion = input('Fecha de Devolución: ')
            registrar_devolucion(id_prestamo, fecha_devolucion)
        elif opcion == 5:
            id_libro = int(input('ID de Libro: '))
            titulo = input('Título (opcional): ')
            autor = input('Autor (opcional): ')
            editorial = input('Editorial (opcional): ')
            anio_publicacion = input('Año de Publicación (opcional): ')
            genero = input('Género (opcional): ')
            cantidad_disponible = input('Cantidad Disponible (opcional): ')
            editar_libro(id_libro, titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible)
        elif opcion == 6:
            id_socio = int(input('ID de Socio: '))
            nombre = input('Nombre (opcional): ')
            apellido = input('Apellido (opcional): ')
            fecha_nacimiento = input('Fecha de Nacimiento (opcional): ')
            direccion = input('Dirección (opcional): ')
            correo_electronico = input('Correo Electrónico (opcional): ')
            telefono = input('Teléfono (opcional): ')
            editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono)
        elif opcion == 7:
            id_libro = int(input('ID de Libro: '))
            eliminar_libro(id_libro)
        elif opcion == 8:
            id_socio = int(input('ID de Socio: '))
            eliminar_socio(id_socio)
        elif opcion == 9:
            campo = input('Campo de búsqueda (titulo, autor, editorial, genero): ')
            valor = input(f'Valor del campo {campo}: ')
            buscar_libro(campo, valor)
        elif opcion == 10:
            campo = input('Campo de búsqueda (nombre, apellido, direccion, correo_electronico, telefono): ')
            valor = input(f'Valor del campo {campo}: ')
            buscar_socio(campo, valor)
        elif opcion == 11:
            id_socio = int(input('ID de Socio: '))
            generar_reporte_por_socio(id_socio)
        elif opcion == 12:
            id_libro = int(input('ID de Libro: '))
            generar_reporte_por_libro(id_libro)
        elif opcion == 13:
            fecha_inicio = input('Fecha de inicio (YYYY-MM-DD): ')
            fecha_fin = input('Fecha de fin (YYYY-MM-DD): ')
            generar_reporte_por_fecha(fecha_inicio, fecha_fin)
        elif opcion == 0:
            break
        else:
            print('Opción no válida.')

if __name__ == '__main__':
    main()

