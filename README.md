Sistema de registro de infracciones de tránsito

Descripción general:

Nombre del proyecto: PythonChallenge
Versión de Python: 3.11
Autor: Lorenzo Ricci
Fecha: 11/06/2024
Repositorio de Github:
https://github.com/lofari/PythonChallenge/
Repositorio de DockerHub: 
https://hub.docker.com/repository/docker/lorenzoricci/django-docker/

Propósito:

Crear un sistema de registro de infracciones utilizando python.

Definiciones y requerimientos:

1. Debe existir una interfaz administrativa, donde puedan manejarse los siguientes registros:
   a. Persona: Campos Nombre y Correo Electrónico						
   b. Vehículo: Campos placa de patente, marca, color. Deben estar relacionados con una persona
   c. Oficial: Nombre y un número único identificatorio
   La interfaz administrativa debe permitir crear, ver, modificar y borrar registros (debe garantizarse la integridad referencial).
2. El sistema debe habilitar una API que permita a una App usada por los oficiales de policía cargar una infracción a un vehículo. Este debe recibir en el body y por método post, un JSON con la siguiente estructura						
   {
   “placa_patente”: “placa patente del vehículo”,
   “timestamp”: “marca de tiempo de la infracción”,
   “comentarios”: “texto libre”						
   }					
   Para la autenticación, la API debe poder generar un token de acceso asociado a cada oficial de policía. Este token debe adjuntarse en Header de la llamada POST, usando la autenticación mediante Bearer Token. Este token puede generarse mediante una interfaz o mediante línea de comandos (en ese caso, documente cómo debe realizarse la llamada).
   El llamado API debe devolver status 200 en caso que todo funcione correctamente, 404 en caso de haber algún parámetro no encontrado (patente que no exista) y 500 si hay un error inesperado. Debe devolver también un mensaje de error apropiado.
3. Debe implementar un método API llamado “generar_informe”, el cual debe recibir como parámetro el correo electrónico de una persona, y devolver un JSON con el listado de infracciones de cualquier vehículo a su nombre. No es necesaria autenticación para este llamado. 						
   Arquitectura:
   Se optó por implementar el sistema utilizando las siguientes tecnologías, aclarando entre paréntesis algunas características que justifican su uso:

Backend:  Django Web Framework (velocidad de desarrollo, integración "out-of-the-box" con BDD y admin)
Base de datos: SQLite (integración "out-of-the-box" con Django)
Autenticación: JWT (estándar Token-Based Auth)
Servidor HTTP: Gunicorn
IaC(Infrastructure as Code): Docker

Pasos para levantar la app:

unicamente ejecutar "python manage.py runserver" o "python3 manage.py runserver" dentro del directorio del proyecto

Credenciales y datos de prueba:

http://localhost:8000/admin
Superuser credentials:
uid: 1234
password: 1234

Persona con vehículo asociado e Infracciones cargadas:
bob@tables.com
patente ABC123


Aclaraciones y consideraciones:

Para los endpoints que requieran autenticación se deberá pedir un token de acceso con las siguientes credenciales (debido a un bug en la implementación del flujo de autenticación los usuarios/oficiales que no son superuser no podrán autenticarse) :
{
"uid": "1234",
"password": "1234"
}

Una vez levantado el proyecto puede encontrar en la siguiente url una interfaz gráfica generada mediante un esquema OpenApi con las especificaciones de todas las rutas dentro de la app y podrá también ejecutar los request:
http://localhost:8000/api/schema/docs


Propuesta Arquitectura AWS
Compute Services: EC2
Database: RDS (Relational Database Service)
API Gateway:  Amazon API Gateway
Authentication and Authorization: IAM
Monitoring and Logging: CloudWatch
Networking: VPC
DNS Routing: Route53

Justificación:
EC2 y RDS: Brindan escalabilidad y flexibilidad para manejar cargas de trabajo variables, y una base de datos relacional gestionada para almacenar datos críticos.
API Gateway: Permite configurar políticas de autenticación y autorización, facilitando la exposición segura de los endpoints de la API.
IAM y CloudWatch: Garantizan la integridad y el rendimiento del sistema mediante seguridad granular basada en roles y monitoreo avanzado.
Route53: DNS routing escalable y de alta disponibilidad
VPC: Seguridad

