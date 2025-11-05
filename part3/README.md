HBnB – Guía de Proyecto

# Propósito del proyecto

HBnB es una aplicación de ejemplo tipo Airbnb, organizada en capas, para practicar:

- Modelo de negocio (Business Logic)

- Persistencia (In-Memory Repository → luego DB)

- API REST (Presentation Layer)

La app maneja entidades principales: User, Place, Review, Amenity.

# Estructura del proyecto

hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py       # Clase base para todas las entidades
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py            # Patrón Facade, maneja lógica y repositorios
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py        # Repositorio en memoria para CRUD
├── run.py                       # Entry point de Flask
├── config.py                     # Configuración de la app
├── requirements.txt
├── README.md

# Capas y responsabilidades


🔹 Models (Business Logic)

base_model.py → Clase base con id, created_at, updated_at.

user.py, place.py, review.py, amenity.py → Clases de negocio con:

Validación de atributos (price >= 0, lat entre -90 y 90, etc.)

Relaciones en memoria (Place conoce reviews y amenities, User conoce places)

Métodos update, edit_* para modificar datos de forma segura.


🔹 Persistence

repository.py → Repositorio en memoria para almacenar objetos:

add, get, get_all, update, delete

get_by_attribute para buscar por un campo

Cada entidad tiene su propio repositorio dentro del Facade.


🔹 Services (Facade)

facade.py → Patrón Facade que centraliza el acceso a los repositorios.

Ejemplo de métodos placeholder:

create_user(user_data)

get_place(place_id)

create_amenity(amenity_data)

La idea: los endpoints de la API nunca hablan directo con el repositorio, siempre usan el Facade.


🔹 API / Presentation

Cada entidad tiene un archivo en api/v1/:

users.py, places.py, reviews.py, amenities.py

Define:

Namespace con Flask-RESTX

Models para validación y Swagger (user_model, place_model, etc.)

Endpoints (GET, POST, PUT) con placeholders de lógica que llaman al Facade.

Ejemplo de endpoint:

@api.route('/<place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        place = facade.get_place(place_id)  # placeholder
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
            'owner': {'id': place.owner.id, 'first_name': place.owner.first_name},
            'amenities': [{'id': a.id, 'name': a.name} for a in place.amenities],
            'reviews': [{'id': r.id, 'text': r.comment, 'rating': r.rating, 'user_id': r.user.id} for r in place.reviews]
        }, 200

# Flujo general

El usuario llama un endpoint (POST /places, GET /users/...)

API valida input con los api.model de Flask-RESTX

API llama al Facade (facade.create_place(data))

Facade interactúa con el repositorio (InMemoryRepository)

Objeto actualizado o creado → se devuelve al endpoint

API devuelve JSON al cliente


# Notas finales

Todos los métodos del Facade que dicen # placeholder no hacen nada todavía, solo sirven para que la API funcione sin errores.

Al implementar la lógica real, asegurar de mantener consistencia:

- Validar existencia de owner y amenities al crear un Place

- Evitar emails duplicados al crear User

- Actualizar updated_at automáticamente

Este README sirve como mapa mental para entender la relación entre capas.