from modulos_comunes.modules_generales import abrir_archivo, escribir_archivo, generar_id

RUTA_PRESTAMOS = 'datos/prestamos.json'

def registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo=None):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    nuevo_prestamo = {
        'id': generar_id(RUTA_PRESTAMOS),
        'id_socio': id_socio,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'costo': costo,
        'fecha_devolucion': None,
        'estado': 'En Curso'
    }
    prestamos.append(nuevo_prestamo)
    escribir_archivo(RUTA_PRESTAMOS, prestamos)
    print(f'Préstamo registrado con éxito.')

def registrar_devolucion(id_prestamo, fecha_devolucion):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    for prestamo in prestamos:
        if prestamo['id'] == id_prestamo:
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo['estado'] = 'Devuelto'
            escribir_archivo(RUTA_PRESTAMOS, prestamos)
            print(f'Devolución registrada con éxito.')
            return
    print('Préstamo no encontrado.')

def generar_reporte_por_socio(id_socio):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if prestamo['id_socio'] == id_socio]
    for prestamo in resultados:
        print(prestamo)

def generar_reporte_por_libro(id_libro):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if prestamo['id_libro'] == id_libro]
    for prestamo in resultados:
        print(prestamo)

def generar_reporte_por_fecha(fecha_inicio, fecha_fin):
    prestamos = abrir_archivo(RUTA_PRESTAMOS)
    resultados = [prestamo for prestamo in prestamos if fecha_inicio <= prestamo['fecha_prestamo'] <= fecha_fin]
    for prestamo in resultados:
        print(prestamo)

