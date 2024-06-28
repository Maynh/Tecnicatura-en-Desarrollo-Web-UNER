from modulos_gestion.libros import registrar_libro, editar_libro, eliminar_libro, buscar_libro_por_id
from modulos_gestion.socios import registrar_socio, editar_socio, eliminar_socio, buscar_socio
from modulos_gestion.prestamos import registrar_prestamo, registrar_devolucion, generar_reporte_por_socio, generar_reporte_por_libro, generar_reporte_por_fecha, generar_reporte_por_socio_pdf, generar_reporte_por_libro_pdf, generar_reporte_todos_socios_pdf, generar_reporte_todos_libros_pdf

def menu():
    print("********* 📚 Bienvenido al Sistema de Gestión de Bibliotecas 📚 *********")
    print("😊 ***Seleccione una opción para progresar con la gestión de la biblioteca*** 😊:")
    print('1: 📖 Registrar Libro')
    print('2: 🧑‍💼 Registrar Socio')
    print('3: 📒 Registrar Préstamo')
    print('4: 🔄 Registrar Devolución')
    print('5: ✏️ Editar Libro')
    print('6: 📝 Editar Socio')
    print('7: ❌ Eliminar Libro')
    print('8: 🗑️ Eliminar Socio')
    print('9: 🔍 Buscar Libro por ID')
    print('10: 🔍 Buscar Socio')
    print('11: 📊 Generar Reporte de Préstamos por Socio')
    print('12: 📊 Generar Reporte de Préstamos por Libro')
    print('13: 📊 Generar Reporte de Préstamos por Fecha')
    print('14: 📊 Generar Reporte de Préstamos por Socio en PDF')
    print('15: 📊 Generar Reporte de Préstamos por Libro en PDF')
    print('16: 📊 Generar Reporte de Todos los Socios en PDF')
    print('17: 📊 Generar Reporte de Todos los Libros en PDF')
    print('0: 🚪 Confirmar y Salir')
    while True:
        try:
            return int(input('Seleccione una opción 👉: '))
        except ValueError:
            print("⚠️ Error: Por favor, ingrese un número válido.")

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            titulo = input('Título: ')
            autor = input('Autor: ')
            editorial = input('Editorial: ')
            anio_publicacion = input('Año de Publicación: ')
            genero = input('Género: ')
            while True:
                try:
                    cantidad_disponible = int(input('Cantidad Disponible: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para la cantidad disponible.")
            registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible)
        elif opcion == 2:
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            fecha_nacimiento = input('Fecha de Nacimiento (YYYY-MM-DD): ')
            direccion = input('Dirección: ')
            correo_electronico = input('Correo Electrónico: ')
            telefono = input('Teléfono: ')
            registrar_socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono)
        elif opcion == 3:
            while True:
                try:
                    id_socio = int(input('ID de Socio: '))
                    id_libro = int(input('ID de Libro: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese números válidos para ID de Socio y ID de Libro.")
            registrar_prestamo(id_socio, id_libro)
        elif opcion == 4:
            while True:
                try:
                    id_prestamo = int(input('ID de Préstamo: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Préstamo.")
            registrar_devolucion(id_prestamo)
        elif opcion == 5:
            while True:
                try:
                    id_libro = int(input('ID de Libro: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Libro.")
            editar_libro(id_libro)
        elif opcion == 6:
            while True:
                try:
                    id_socio = int(input('ID de Socio: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Socio.")
            editar_socio(id_socio)
        elif opcion == 7:
            while True:
                try:
                    id_libro = int(input('ID de Libro: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Libro.")
            eliminar_libro(id_libro)
        elif opcion == 8:
            while True:
                try:
                    id_socio = int(input('ID de Socio: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Socio.")
            eliminar_socio(id_socio)
        elif opcion == 9:
            while True:
                try:
                    id_libro = int(input('ID de Libro: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Libro.")
            buscar_libro_por_id(id_libro)
        elif opcion == 10:
            buscar_socio()
        elif opcion == 11:
            while True:
                try:
                    id_socio = int(input('ID de Socio: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Socio.")
            generar_reporte_por_socio(id_socio)
        elif opcion == 12:
            while True:
                try:
                    id_libro = int(input('ID de Libro: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Libro.")
            generar_reporte_por_libro(id_libro)
        elif opcion == 13:
            fecha_inicio = input('Fecha de inicio (YYYY-MM-DD): ')
            fecha_fin = input('Fecha de fin (YYYY-MM-DD): ')
            generar_reporte_por_fecha(fecha_inicio, fecha_fin)
        elif opcion == 14:
            while True:
                try:
                    id_socio = int(input('ID de Socio: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Socio.")
            generar_reporte_por_socio_pdf(id_socio)
        elif opcion == 15:
            while True:
                try:
                    id_libro = int(input('ID de Libro: '))
                    break
                except ValueError:
                    print("⚠️ Error: Por favor, ingrese un número válido para el ID de Libro.")
            generar_reporte_por_libro_pdf(id_libro)
        elif opcion == 16:
            generar_reporte_todos_socios_pdf()
        elif opcion == 17:
            generar_reporte_todos_libros_pdf()
        elif opcion == 0:
            print("👋 Adiós! Gracias por usar el Sistema de Gestión de Bibliotecas.")
            break
        else:
            print('⚠️ Opción no válida.')

if __name__ == '__main__':
    main()
