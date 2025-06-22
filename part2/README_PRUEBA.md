# HolbertonBnB - Part 2

Este proyecto corresponde a la segunda parte del proyecto HolbertonBnB, inspirado en AirBnB y desarrollado como parte del programa de Holberton School. Su objetivo principal es implementar una API RESTful usando Flask y Flask-RESTx, aplicando principios de programación orientada a objetos y una arquitectura limpia con patrones como Repository y Facade.

La API permite gestionar usuarios, propiedades (places), servicios (amenities) y reseñas (reviews), estructurando el sistema de forma modular, testeable y escalable.

## Autores

- @GeronimoNegreira  
- @AgustinLahalo  
- @BruDosSant

---

## Requisitos e instalación

### Requisitos previos

- Python 3.x  
- pip

### Instalación

```bash
git clone <url-del-repo>
cd parte2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Ejecución
bash
Copiar
Editar
python3 run.py
La API estará disponible en: http://127.0.0.1:5000/

Estructura del Proyecto
bash
Copiar
Editar
parte2/
├── app/
│   ├── api/v1/              # Endpoints REST organizados por recurso
│   ├── models/              # Entidades y lógica de validación
│   ├── persistence/         # Lógica de almacenamiento en memoria
│   ├── services/            # Fachada de servicios de negocio
├── config.py                # Configuración general
├── run.py                   # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias
Arquitectura del Sistema
El sistema está organizado en capas:

Presentación (API): Maneja solicitudes y respuestas HTTP, formatea datos y gestiona errores.

Lógica de Negocio (Facade): Aplica reglas del sistema y coordina operaciones sobre entidades.

Persistencia (Repository): Administra el almacenamiento de datos (in-memory).

Se implementa el patrón fachada, que permite desacoplar la API de la lógica interna, proporcionando una interfaz clara para interactuar con los datos y reglas del negocio.

Entidades Principales
User: Usuario registrado en la plataforma.

Place: Propiedad que un usuario publica.

Amenity: Servicios asociados a un lugar (WiFi, piscina, etc.).

Review: Comentario y puntuación sobre un lugar.

BaseModel: Clase abstracta que aporta atributos comunes (id, created_at, updated_at).

Validaciones implementadas
Email válido (debe contener @ y .).

Nombre y apellido con máximo 50 caracteres.

Precio debe ser positivo.

Coordenadas dentro de los rangos válidos.

Puntuación de reseñas entre 1 y 5 estrellas.

Endpoints disponibles
Método	Ruta	Descripción
POST	/api/v1/users/	Crear un nuevo usuario
GET	/api/v1/users/<user_id>	Obtener info de un usuario
PUT	/api/v1/users/<user_id>	Actualizar info de un usuario
POST	/api/v1/places/	Crear un nuevo lugar
GET	/api/v1/places/	Listar todos los lugares
GET	/api/v1/places/<place_id>	Obtener info de un lugar
PUT	/api/v1/places/<place_id>	Actualizar un lugar
POST	/api/v1/amenities/	Crear un nuevo servicio
GET	/api/v1/amenities/	Listar todos los servicios
GET	/api/v1/amenities/<amenity_id>	Obtener info de un servicio
PUT	/api/v1/amenities/<amenity_id>	Actualizar un servicio
POST	/api/v1/reviews/	Crear una reseña
GET	/api/v1/reviews/	Listar todas las reseñas
GET	/api/v1/reviews/<review_id>	Obtener una reseña
PUT	/api/v1/reviews/<review_id>	Actualizar una reseña
DELETE	/api/v1/reviews/<review_id>	Eliminar una reseña
GET	/api/v1/places/<place_id>/reviews	Listar reseñas de un lugar

Flujo de Datos - Ejemplo
Registrar un usuario:

Cliente envía solicitud POST /users/ con datos JSON.

La API valida los datos y llama a facade.create_user().

Se instancia y almacena un nuevo objeto User.

Se responde con un JSON de confirmación.

Crear una reseña:

Cliente envía POST /reviews/ con texto y puntaje.

Se valida la existencia de user y place.

Se guarda la reseña y se vincula al lugar.

Se devuelve la reseña creada.

Tests
Para ejecutar los tests automatizados:

bash
Copiar
Editar
python3 -m unittest discover tests/
Cada archivo de prueba cubre escenarios correctos e incorrectos para los endpoints de la API.

yaml
Copiar
Editar

---

Copialo y pegalo en tu archivo `README.md`. ¿Querés que también te genere una versión en inglés o te ayudo con documentación Swagger o ejemplos curl?







Dijiste:
no le haz hecho una descripcion al projecto


ChatGPT dijo:
Tenés toda la razón. El título dice "HolbertonBnB - Part 2", pero falta una descripción más clara y redactada como introducción. A continuación, te dejo el bloque completo con el título y una buena descripción de proyecto que podés pegar al inicio del README.md:

markdown
Copiar
Editar
# HolbertonBnB - Part 2

Este proyecto es la continuación de **HolbertonBnB**, una aplicación inspirada en el funcionamiento de plataformas como AirBnB. Desarrollado como parte del programa de estudios de Holberton School, el objetivo de esta segunda parte es crear una **API RESTful** utilizando **Flask** y **Flask-RESTx**, aplicando conceptos clave como:

- Arquitectura en capas
- Principios de diseño SOLID
- Programación orientada a objetos
- Patrones como **Repository** y **Facade**

La API permite gestionar de manera estructurada los principales recursos del sistema: **usuarios**, **propiedades (places)**, **servicios adicionales (amenities)** y **reseñas (reviews)**. Toda la lógica está organizada para permitir modularidad, testeo y escalabilidad futura.