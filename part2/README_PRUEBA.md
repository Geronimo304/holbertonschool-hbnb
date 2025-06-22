# HolbertonBnB - Parte 2

Este proyecto es la continuación de **HolbertonBnB**, una aplicación inspirada en el funcionamiento de plataformas como AirBnB. Desarrollado como parte del programa de estudios de **Holberton School**, el objetivo de esta segunda parte es construir una **API RESTful** utilizando **Flask** y **Flask-RESTx**, aplicando principios de diseño como:

- Arquitectura en capas
- Programación orientada a objetos
- Principios SOLID
- Patrones como **Repository** y **Facade**

La API permite gestionar los siguientes recursos: **usuarios**, **propiedades (places)**, **servicios (amenities)** y **reseñas (reviews)**. Todo el sistema está diseñado para ser modular, testeable y escalable.

---

##  Estructura del Proyecto

```
parte2/
├── app/
│   ├── api/v1/              # Endpoints REST organizados por recurso
│   ├── models/              # Entidades y validaciones
│   ├── persistence/         # Almacenamiento en memoria (repositories)
│   ├── services/            # Lógica de negocio (facades)
├── config.py                # Configuración global
├── run.py                   # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
```

---

##  Requisitos e Instalación

### Prerrequisitos

- Python 3.x  
- `pip`  
- `virtualenv` (opcional pero recomendado)

### Instalación

```bash
git clone <url-del-repo>
cd parte2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Ejecución

```bash
python3 run.py
```

La API estará disponible en: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

##  Arquitectura del Sistema

El sistema sigue una arquitectura por capas:

- **Presentación (API)**: Maneja solicitudes/respuestas HTTP y errores.
- **Lógica de Negocio (Facade)**: Aplica reglas y coordina entidades.
- **Persistencia (Repository)**: Gestión del almacenamiento (in-memory).

> Se utiliza el patrón **Facade** para desacoplar la API de la lógica interna, exponiendo una interfaz clara.

---

##  Entidades Principales

- **User**: Usuario registrado en la plataforma.
- **Place**: Propiedad que publica un usuario.
- **Amenity**: Servicio opcional para un lugar (WiFi, piscina, etc.).
- **Review**: Comentario y puntuación de un lugar.
- **BaseModel**: Clase base con atributos comunes (`id`, `created_at`, `updated_at`).

---

##  Validaciones

- Email debe contener `@` y `.`.
- Nombre y apellido: máximo 50 caracteres.
- Precio: debe ser un número positivo.
- Coordenadas geográficas válidas.
- Puntuación de reseñas: de 1 a 5 estrellas.

---

##  Endpoints Disponibles

| Método | Ruta                                     | Descripción                             |
|--------|------------------------------------------|-----------------------------------------|
| POST   | `/api/v1/users/`                         | Crear un nuevo usuario                  |
| GET    | `/api/v1/users/<user_id>`                | Obtener info de un usuario              |
| PUT    | `/api/v1/users/<user_id>`                | Actualizar info de un usuario           |
| POST   | `/api/v1/places/`                        | Crear un nuevo lugar                    |
| GET    | `/api/v1/places/`                        | Listar todos los lugares                |
| GET    | `/api/v1/places/<place_id>`             | Obtener info de un lugar                |
| PUT    | `/api/v1/places/<place_id>`             | Actualizar un lugar                     |
| POST   | `/api/v1/amenities/`                     | Crear un nuevo servicio                 |
| GET    | `/api/v1/amenities/`                     | Listar todos los servicios              |
| GET    | `/api/v1/amenities/<amenity_id>`         | Obtener info de un servicio             |
| PUT    | `/api/v1/amenities/<amenity_id>`         | Actualizar un servicio                  |
| POST   | `/api/v1/reviews/`                       | Crear una reseña                        |
| GET    | `/api/v1/reviews/`                       | Listar todas las reseñas                |
| GET    | `/api/v1/reviews/<review_id>`            | Obtener una reseña                      |
| PUT    | `/api/v1/reviews/<review_id>`            | Actualizar una reseña                   |
| DELETE | `/api/v1/reviews/<review_id>`            | Eliminar una reseña                     |
| GET    | `/api/v1/places/<place_id>/reviews`      | Listar reseñas de un lugar              |

---

##  Flujo de Datos - Ejemplos

### Registrar un usuario

1. Cliente hace `POST /api/v1/users/` con datos JSON.
2. Se validan los datos.
3. Se llama a `facade.create_user()`.
4. Se instancia y guarda el objeto `User`.
5. Se devuelve un JSON de respuesta.

### Crear una reseña

1. Cliente hace `POST /api/v1/reviews/`.
2. Se valida que el `user_id` y `place_id` existan.
3. Se almacena la reseña y se asocia al lugar.
4. Se responde con los datos de la reseña.

---

##  Tests

Para correr los tests:

```bash
python3 -m unittest discover tests/
```

Cada archivo de test incluye casos exitosos y de error para los endpoints de la API.

---

##  Autores

- GeronimoNegreira
- AgustinLahalo
- BruDosSant

---
