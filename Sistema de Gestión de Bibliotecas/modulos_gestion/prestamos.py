from modulos_comunes.modules_generales import abrir_archivo, guardar_datos, generar_id
from datetime import datetime, timedelta

RUTA_PRESTAMOS = 'datos/prestamos.json'

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
            print(f"📘 ID Préstamo: {prestamo['id']}, ID Libro: {prestamo['id_libro']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
    else:
        print(f'❌ No se encontraron préstamos para el socio con ID {id_socio}.')

def generar_reporte_por_libro(id_libro):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if prestamo['id_libro'] == id_libro]
    if resultados:
        print(f'📊 Reporte de préstamos para el libro con ID {id_libro}:')
        for prestamo in resultados:
            print(f"📘 ID Préstamo: {prestamo['id']}, ID Socio: {prestamo['id_socio']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
    else:
        print(f'❌ No se encontraron préstamos para el libro con ID {id_libro}.')

def generar_reporte_por_fecha(fecha_inicio, fecha_fin):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if fecha_inicio <= prestamo['fecha_prestamo'] <= fecha_fin]
    if resultados:
        print(f'📊 Reporte de préstamos desde {fecha_inicio} hasta {fecha_fin}:')
        for prestamo in resultados:
            print(f"📘 ID Préstamo: {prestamo['id']}, ID Socio: {prestamo['id_socio']}, ID Libro: {prestamo['id_libro']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}, Estado: {prestamo['estado']}, Costo: {prestamo['costo']}")
    else:
        print(f'❌ No se encontraron préstamos entre {fecha_inicio} y {fecha_fin}.')





