# Tecnicatura-en-Desarrollo-Web-UNER
Trabajo Final Integrador
# Sistema de Gestión de Bibliotecas
# Instalar dependencias desde requirements.txt:
# pip install -r requirements.txt



![Biblioteca Virtual](https://eservicioseducativos.com/wp-content/uploads/2021/04/bibliotecas-digitales1.jpg)
# Equipo de Desarrollo: Estudiantes de la UTN-FRSR
- **Roveres Julieta**
- **Anabella Broese**
- **Medina Mayra**
- **Saidi Taoufik**
## Descripción
Este proyecto es una solución de software para gestionar el préstamo y devolución de libros en una biblioteca. Fue desarrollado como parte del trabajo integrador final por un equipo de 4 estudiantes de la UTN-FRSR.

## Objetivo
Desarrollar una solución de software que permita:
- Registrar, editar y eliminar libros.
- Registrar, editar y eliminar socios.
- Registrar préstamos y devoluciones.
- Búsqueda de libros por título, género, autor y editorial.
- Generar reportes de préstamos y devoluciones por socio, libro y rango de fechas.

## Requerimientos
- **Registro de Libros**:
  - ID de Libro (número único y autoincremental)
  - Título
  - Autor
  - Editorial
  - Año de Publicación
  - Género
  - Cantidad Disponible

- **Gestión de Socios**:
  - ID de Socio (número único y autoincremental)
  - Nombre
  - Apellido
  - Fecha de Nacimiento
  - Dirección
  - Correo Electrónico
  - Teléfono

- **Registro de Préstamos y Devoluciones**:
  - ID de Préstamo (número único y autoincremental)
  - ID de Socio
  - ID de Libro
  - Fecha de Préstamo
  - Costo (en caso de que tuviera)
  - Fecha de Devolución
  - Estado del Préstamo (En Curso/Devuelto)

## Características del Software
- Almacenamiento de Información: Utilización de archivos JSON para almacenar los datos solicitados.
- Interfaces de usuario interactivas que permitan:
  - Registrar, editar y eliminar libros.
  - Registrar, editar y eliminar socios.
  - Registrar préstamos y devoluciones.
  - Búsqueda de libros por título, género, autor y editorial.
  - Generar reportes de préstamos y devoluciones por socio, libro y rango de fechas.
- Funcionalidad extra a criterio del grupo.

- **Nuevas Funcionalidades**:
- Generar_reporte_por_socio_pdf(id_socio): Genera un reporte en PDF de los préstamos de un socio específico.
- Generar_reporte_por_libro_pdf(id_libro): Genera un reporte en PDF de los préstamos de un libro específico.
- Generar_reporte_todos_socios_pdf(): Genera un reporte en PDF de todos los socios registrados.
- Generar_reporte_todos_libros_pdf(): Genera un reporte en PDF de todos los libros disponibles en la biblioteca.


## Requisitos del Sistema

- Python 3.7 o superior.
- Librerías de Python:
  - `json`
  - `os` 
  - `datetime` 
  - `reportlab` (para generar reportes en PDF)