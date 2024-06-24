import json
import os

def abrir_archivo(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def guardar_datos(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

def generar_id(ruta):
    datos = abrir_archivo(ruta)
    if not datos:
        return 1
    return max(item['id'] for item in datos) + 1


