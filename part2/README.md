
# HolbertonBnB - Part 2

## Project Description

This is the second part of the HolbertonBnB project, inspired by AirBnB, developed as part of the Holberton School curriculum. The objective in this phase is to implement a RESTful API using Flask and Flask-RESTx, apply object-oriented principles, and structure the application using clean architecture and design patterns like Repository and Facade. The API allows managing users, places, amenities, and reviews in a modular, testable, and extensible way.

## Repository Structure

The repository is structured as follows:

- **app/**: Main application package.

  - **api/**: RESTful API endpoints grouped by resource.
    - `v1/`: API version 1 with namespaces for users, places, amenities, and reviews.
  
  - **models/**: Contains entity classes and business rules.
    - `basemodel.py`: Base class with shared attributes and methods.
    - `user.py`, `place.py`, `review.py`, `amenity.py`: Entity definitions with validation logic.
  
  - **persistence/**: Handles in-memory data storage.
    - `repository.py`: Implements the Repository pattern for CRUD operations.
  
  - **services/**: Business logic layer.
    - `facade.py`: Central facade class to coordinate between repositories and API.

- **tests/**: Unit tests for all API endpoints.
  - `test_user_endpoints.py`, `test_place_endpoints.py`, etc.

- **config.py**: Application configuration settings.

- **run.py**: Entry point to launch the API.

- **requeriments.txt**: List of required Python packages.

## System Architecture

This project follows a layered architecture:

- **Presentation Layer (API)**: Handles HTTP requests and responses.
- **Business Logic Layer (Facade)**: Applies system rules and orchestrates operations.
- **Persistence Layer (Repository)**: Provides storage functionality (in-memory in this phase).

Each layer is designed to be independent and interchangeable, which supports scalability and future upgrades (e.g., replacing in-memory storage with a database).

## Class Overview

The main entities of the system include:

- `User`: Represents a registered user of the platform.
- `Place`: A property listed by a user.
- `Amenity`: Extra features associated with a place.
- `Review`: Feedback left by a user about a place.
- `BaseModel`: Abstract class that handles common attributes like `id`, `created_at`, and `updated_at`.

## Installation and Configuration

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip

### Install Dependencies

```bash
pip install -r requeriments.txt
```

### Run the Application

```bash
python3 run.py
```

The API will be available at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Example Endpoints

- `POST /api/v1/users/` – Create a new user  
- `GET /api/v1/places/` – List all places  
- `POST /api/v1/reviews/` – Add a review to a place  
- `PUT /api/v1/amenity/<id>` – Update an amenity

## Testing

You can run the tests using:

```bash
python3 -m unittest discover tests/
```

Each test file validates both correct and incorrect behavior of the API.

## Authors

[@GeronimoNegreira](https://github.com/Geronimo304)  
[@AgustinLahalo](https://github.com/AgustinLahalo)  
[@BruDosSant](https://github.com/BruDosSant)
