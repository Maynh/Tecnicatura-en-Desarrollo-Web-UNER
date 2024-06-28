# Tecnicatura-en-Desarrollo-Web-UNER
Trabajo Final Integrador
# Sistema de Gestión de Bibliotecas


![Descripción de la imagen](https://ar.images.search.yahoo.com/images/view;_ylt=AwrNYt3z13RmLhIWx42t9Qt.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkA2Y1ZjhkN2RlMDIxZTE2YzJkZTZkOWI0MjcyYjBmYzU0BGdwb3MDMwRpdANiaW5n?back=https%3A%2F%2Far.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dimagen%2Bde%2Buna%2Bbiblioteca%2Bvirtual%26type%3DE210AR91215G0%26fr%3Dmcafee%26fr2%3Dpiv-web%26tab%3Dorganic%26ri%3D3&w=800&h=500&imgurl=estudiantes.ucontinental.edu.pe%2Fwp-content%2Fuploads%2F2019%2F01%2Fbiblioteca-virtual-3.jpg&rurl=https%3A%2F%2Festudiantes.ucontinental.edu.pe%2Fservicios%2Fbiblioteca-virtual%2F&size=74.6KB&p=imagen+de+una+biblioteca+virtual&oid=f5f8d7de021e16c2de6d9b4272b0fc54&fr2=piv-web&fr=mcafee&tt=Biblioteca+Virtual+%E2%80%93+Portal+del+Estudiante+de+la+Universidad+Continental&b=0&ni=21&no=3&ts=&tab=organic&sigr=q.qimh6YjIDq&sigb=5XVci7.zfSTX&sigi=MJ1TTUcGvUzj&sigt=KoHXrTQurldY&.crumb=Vpw4vpGK8Ns&fr=mcafee&fr2=piv-web&type=E210AR91215G0)

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
