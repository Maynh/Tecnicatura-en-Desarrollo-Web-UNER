from modulos_comunes.modules_generales import abrir_archivo, guardar_datos, generar_id
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

RUTA_PRESTAMOS = 'datos/prestamos.json'
RUTA_SOCIOS = 'datos/socios.json'
RUTA_LIBROS = 'datos/libros.json'


def registrar_prestamo(id_socio, id_libro, costo=None):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    fecha_prestamo = datetime.now().strftime('%Y-%m-%d')
    nuevo_prestamo = {
        'id': generar_id(RUTA_PRESTAMOS),
        'id_socio': id_socio,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'costo': costo,
        'fecha_devolucion': (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d'),
        'estado': 'En Curso'
    }
    prestamos.append(nuevo_prestamo)
    guardar_datos(RUTA_PRESTAMOS, prestamos)
    print(f'📚 Préstamo registrado con éxito.')


def registrar_devolucion(id_prestamo):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    fecha_devolucion = datetime.now().strftime('%Y-%m-%d')
    for prestamo in prestamos:
        if prestamo['id'] == id_prestamo:
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo['estado'] = 'Devuelto'
            guardar_datos(RUTA_PRESTAMOS, prestamos)
            print(f'🔄 Devolución registrada con éxito.')
            return
    print('❌ Préstamo no encontrado.')


def generar_reporte_por_socio(id_socio):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if prestamo['id_socio'] == id_socio]
    if resultados:
        print(f'📊 Reporte de préstamos para el socio con ID {id_socio}:')
        for prestamo in resultados:
            print(
                f"📘 ID Préstamo: {prestamo['id']}, ID Libro: {prestamo['id_libro']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
    else:
        print(f'❌ No se encontraron préstamos para el socio con ID {id_socio}.')


def generar_reporte_por_libro(id_libro):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if prestamo['id_libro'] == id_libro]
    if resultados:
        print(f'📊 Reporte de préstamos para el libro con ID {id_libro}:')
        for prestamo in resultados:
            print(
                f"📘 ID Préstamo: {prestamo['id']}, ID Socio: {prestamo['id_socio']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
    else:
        print(f'❌ No se encontraron préstamos para el libro con ID {id_libro}.')


def generar_reporte_por_fecha(fecha_inicio, fecha_fin):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if fecha_inicio <= prestamo['fecha_prestamo'] <= fecha_fin]
    if resultados:
        print(f'📊 Reporte de préstamos desde {fecha_inicio} hasta {fecha_fin}:')
        for prestamo in resultados:
            print(
                f"📘 ID Préstamo: {prestamo['id']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
    else:
        print(f'❌ No se encontraron préstamos entre {fecha_inicio} y {fecha_fin}.')


def generar_reporte_por_socio_pdf(id_socio):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    socios = abrir_archivo(RUTA_SOCIOS)
    libros = abrir_archivo(RUTA_LIBROS)

    socio = None
    for s in socios:
        if s['id'] == id_socio:
            socio = s
            break

    if not socio:
        print(f'❌ Socio con ID {id_socio} no encontrado.')
        return

    resultados = []
    for prestamo in prestamos:
        if prestamo['id_socio'] == id_socio:
            resultados.append(prestamo)

    if resultados:
        archivo_pdf = f'reporte_prestamos_socio_{id_socio}.pdf'
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(30, 750, f'📊 Reporte de Préstamos para Socio ID {id_socio}')
        c.drawString(30, 735, f"Nombre: {socio['nombre']} {socio['apellido']}")
        c.drawString(30, 720, f"Correo: {socio['correo_electronico']}")
        c.drawString(30, 705, '*' * 80)
        y = 690
        for prestamo in resultados:
            libro = None
            for l in libros:
                if l['id'] == prestamo['id_libro']:
                    libro = l
                    break
            if libro:
                c.drawString(30, y, f"📘 ID Préstamo: {prestamo['id']}")
                y -= 15
                c.drawString(30, y, f"ID Libro: {prestamo['id_libro']}, Título: {libro['titulo']}")
                y -= 15
                c.drawString(30, y, f"Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}")
                y -= 15
                c.drawString(30, y, f"Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
                y -= 30
        c.save()
        print(f'📊 Reporte en PDF generado con éxito: {archivo_pdf}')
    else:
        print(f'❌ No se encontraron préstamos para el socio con ID {id_socio}.')


def generar_reporte_por_libro_pdf(id_libro):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    socios = abrir_archivo(RUTA_SOCIOS)
    libros = abrir_archivo(RUTA_LIBROS)

    libro = None
    for l in libros:
        if l['id'] == id_libro:
            libro = l
            break

    if not libro:
        print(f'❌ Libro con ID {id_libro} no encontrado.')
        return

    resultados = []
    for prestamo in prestamos:
        if prestamo['id_libro'] == id_libro:
            resultados.append(prestamo)

    if resultados:
        archivo_pdf = f'reporte_prestamos_libro_{id_libro}.pdf'
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(30, 750, f'📊 Reporte de Préstamos para Libro ID {id_libro}')
        c.drawString(30, 735, f"Título: {libro['titulo']}")
        c.drawString(30, 720, f"Autor: {libro['autor']}")
        c.drawString(30, 705, '*' * 80)
        y = 690
        for prestamo in resultados:
            socio = None
            for s in socios:
                if s['id'] == prestamo['id_socio']:
                    socio = s
                    break
            if socio:
                c.drawString(30, y, f"📘 ID Préstamo: {prestamo['id']}")
                y -= 15
                c.drawString(30, y, f"ID Socio: {prestamo['id_socio']}, Nombre: {socio['nombre']} {socio['apellido']}")
                y -= 15
                c.drawString(30, y, f"Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}")
                y -= 15
                c.drawString(30, y, f"Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
                y -= 30
        c.save()
        print(f'📊 Reporte en PDF generado con éxito: {archivo_pdf}')
    else:
        print(f'❌ No se encontraron préstamos para el libro con ID {id_libro}.')


def generar_reporte_todos_socios_pdf():
    socios = abrir_archivo(RUTA_SOCIOS)

    if socios:
        archivo_pdf = 'reporte_todos_socios.pdf'
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(30, 750, '📊 Reporte de Todos los Socios Registrados')
        c.drawString(30, 735, '-*' * 80)
        y = 720
        for socio in socios:
            c.drawString(30, y, f"ID Socio: {socio['id']}")
            y -= 15
            c.drawString(30, y, f"Nombre: {socio['nombre']} {socio['apellido']}")
            y -= 15
            c.drawString(30, y, f"Fecha Nacimiento: {socio['fecha_nacimiento']}")
            y -= 15
            c.drawString(30, y, f"Dirección: {socio['direccion']}")
            y -= 15
            c.drawString(30, y, f"Correo: {socio['correo_electronico']}")
            y -= 15
            c.drawString(30, y, f"Teléfono: {socio['telefono']}")
            y -= 30
        c.save()
        print(f'📊 Reporte en PDF generado con éxito: {archivo_pdf}')
    else:
        print(f'❌ No se encontraron socios registrados.')


def generar_reporte_todos_libros_pdf():
    libros = abrir_archivo(RUTA_LIBROS)

    if libros:
        archivo_pdf = 'reporte_todos_libros.pdf'
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(30, 750, '📊 Reporte de Todos los Libros Disponibles')
        c.drawString(30, 735, '-*' * 80)
        y = 720
        for libro in libros:
            c.drawString(30, y, f"ID Libro: {libro['id']}")
            y -= 15
            c.drawString(30, y, f"Título: {libro['titulo']}")
            y -= 15
            c.drawString(30, y, f"Autor: {libro['autor']}")
            y -= 15
            c.drawString(30, y, f"Editorial: {libro['editorial']}")
            y -= 15
            c.drawString(30, y, f"Año de Publicación: {libro['anio_publicacion']}")
            y -= 15
            c.drawString(30, y, f"Género: {libro['genero']}")
            y -= 15
            c.drawString(30, y, f"Cantidad Disponible: {libro['cantidad_disponible']}")
            y -= 30
        c.save()
        print(f'📊 Reporte en PDF generado con éxito: {archivo_pdf}')
    else:
        print(f'❌ No se encontraron libros disponibles.')








