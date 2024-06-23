from modulos_comunes.modules_generales import abrir_archivo, escribir_archivo, generar_id

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
    escribir_archivo(RUTA_SOCIOS, socios)
    print(f'Socio "{nombre} {apellido}" registrado con éxito.')

def editar_socio(id_socio, nombre=None, apellido=None, fecha_nacimiento=None, direccion=None, correo_electronico=None, telefono=None):
    socios = abrir_archivo(RUTA_SOCIOS)
    for socio in socios:
        if socio['id'] == id_socio:
            if nombre: socio['nombre'] = nombre
            if apellido: socio['apellido'] = apellido
            if fecha_nacimiento: socio['fecha_nacimiento'] = fecha_nacimiento
            if direccion: socio['direccion'] = direccion
            if correo_electronico: socio['correo_electronico'] = correo_electronico
            if telefono: socio['telefono'] = telefono
            escribir_archivo(RUTA_SOCIOS, socios)
            print(f'Socio con ID {id_socio} editado con éxito.')
            return
    print(f'Socio con ID {id_socio} no encontrado.')

def eliminar_socio(id_socio):
    socios = abrir_archivo(RUTA_SOCIOS)
    socios = [socio for socio in socios if socio['id'] != id_socio]
    escribir_archivo(RUTA_SOCIOS, socios)
    print(f'Socio con ID {id_socio} eliminado con éxito.')

def buscar_socio(campo, valor):
    socios = abrir_archivo(RUTA_SOCIOS)
    resultados = [socio for socio in socios if socio[campo] == valor]
    for socio in resultados:
        print(socio)

