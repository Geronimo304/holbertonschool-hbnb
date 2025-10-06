# Documentación Técnica del Proyecto HBnB

## Clon de AirBnB: Una Plataforma para la Gestión de Alojamientos  
**Autores:** Sofia Nunez, Martin Suarez, Geronimo Negreira – #C27

---

## Introducción

Este documento sirve como el plan detallado y la referencia técnica para el desarrollo del proyecto **HBnB** (un clon simplificado de AirBnB).  
Su objetivo es consolidar los diagramas de arquitectura, el diseño de la lógica de negocio y los flujos de interacción de la API, para guiar la implementación y asegurar que todos los desarrolladores tengan una comprensión clara y unificada del sistema.

---

## 1. Arquitectura de Alto Nivel

Esta sección presenta la vista general de la aplicación, mostrando cómo se organizan los principales componentes.

### Diagrama de Paquetes de Alto Nivel

El siguiente diagrama ilustra la arquitectura de tres capas y cómo la **Fachada** actúa como el punto de contacto entre la **Presentación** y la **Lógica de Negocio**.

![Diagrama de Paquetes de Alto Nivel](WhatsApp%20Image%202025-10-02%20at%2010.51.18%20AM.jpeg)

---

### Explicación de la Arquitectura

El proyecto **HBnB** sigue una **Arquitectura de Capas (Layered Architecture)** para separar responsabilidades, lo que hace que el código sea más manejable, modular y escalable.

#### Capa de Presentación / API (Presentation Layer)
- Contiene los servicios (+ ServiceAPI) y endpoints que manejan las peticiones del usuario.  
- No contiene lógica de negocio; su rol es recibir la petición, pre-validarla (formato) y pasarla a la capa inferior.

#### Capa de Fachada (Facade)
- El vínculo "Facade Pattern" indica que la Capa de Presentación usa un patrón de diseño que simplifica el acceso a la lógica de negocio, ofreciendo una interfaz unificada y desacoplando las dos capas.

#### Capa de Lógica de Negocio (Business Logic Layer)
- El núcleo de la aplicación.  
- Contiene las clases principales del sistema (+ Place, + User, + Review, + Amenity) y las reglas de negocio.  
- Define cómo se comportan y relacionan las entidades del sistema.

#### Capa de Persistencia (Persistence Layer)
- Contiene el acceso a la base de datos (+ DatabaseAccess).  
- Es la única capa que interactúa directamente con la base de datos.

---

### Racional del Diseño

Esta separación en capas es crucial porque:
- Permite desarrollar, probar y mantener cada capa de forma aislada.  
- Mejora la modularidad, reusabilidad y robustez del sistema.  
- Facilita la incorporación de nuevas tecnologías (como un nuevo tipo de base de datos) sin romper el resto de la arquitectura.

---

## 2. Capa de Lógica de Negocio

Esta capa define las entidades del sistema, sus atributos, métodos y sus relaciones.

### Diagrama de Clases Detallado

El diagrama a continuación es la representación visual de la lógica de negocio central de **HBnB**, incluyendo las entidades, sus atributos y sus relaciones con multiplicidad (por ejemplo, 1..*).

![Diagrama de Clases Detallado](WhatsApp%20Image%202025-10-03%20at%203.27.22%20PM.jpeg)

---

### Explicación del Modelo de Datos

El diagrama de clases muestra las principales entidades (Modelos) que definen el proyecto y sus relaciones.  
Todas las clases clave (**Place**, **Review**, **Amenity**) heredan de la clase base común **Base**, la cual provee la estructura de identidad del objeto.

#### Principales Clases del Sistema

**Base:**  
Provee los atributos esenciales de seguimiento:  
- +str uid (UUID único, que funciona como id).  
- +int up (Representa timestamps como created_at o updated_at).

**User:**  
Representa a un usuario o anfitrión.  
- Atributos: `name`, `lastname`, `age`, `password`.  
- Métodos de negocio: `+postPlace(place: Places)`, `+bookPlace(place: Places)`, `+makeReview(review: Review, place: Places)`.  
- Relación: `1 owns 0..* Place`, `1 writes 0..* Review`.

**Place:**  
El alojamiento ofrecido.  
- Atributos: `coordinates (tuple)`, `description`, `amenities (list)`, `price`, `owner (User)`.  
- Método de negocio: `+addAmenity(amenity: Amenity)`.  
- Relación: `1 has 0..* Amenity`, `1 receives 0..* Review`.

**Review:**  
Reseña de un `User` sobre un `Place`.  
- Atributos: `rating (int)`, `comment (str)`, `reviewer (User)`, `place (Place)`.

**Amenity:**  
Representa los servicios disponibles (`list name`).

---

### Decisiones de Diseño

- **Herencia de Base:**  
  El uso de la clase `Base` asegura que las clases del negocio (`Place`, `Review`, `Amenity`) compartan campos fundamentales para la persistencia (como el `uid`), manteniendo la coherencia del modelo.  

- **Relaciones Claras:**  
  La multiplicidad asegura la integridad de los datos; por ejemplo, un `Place` debe ser propiedad de exactamente un `User` (`1 owns 0..* Place`).

---

## 3. Flujo de Interacción de la API

Esta sección ilustra cómo fluyen las peticiones de datos entre los diferentes componentes del sistema al interactuar con la API.

### Diagramas de Secuencia para Llamadas API

Los diagramas detallan la secuencia de eventos (mensajes) entre los actores (`User`) y los subsistemas (`API`, `Business Logic`, `Persistence Layer`, `Database`) para cumplir con una petición.

---

### 3.1 Creación de Recursos  
**(Ejemplos: Registrar Usuario, Crear Place, Enviar Review)**  

Este flujo genérico, que culmina en el código **HTTP 201 (Created)**, ilustra la validación en múltiples capas antes de la persistencia.

| Diagrama | Propósito | Código de Éxito | Código de Error |
|-----------|------------|----------------|----------------|
| ![User Registration](WhatsApp%20Image%202025-10-02%20at%2010.51.34%20AM%20(1).jpeg) | User Registration | 201 | 400 (Error in provided data) |
| ![Place Creation](WhatsApp%20Image%202025-10-02%20at%2010.51.34%20AM.jpeg) | Place Creation | 201 | 400 (Error in provided data) |
| ![Review Submission](WhatsApp%20Image%202025-10-02%20at%2010.51.33%20AM%20(1).jpeg) | Review Submission | 201 | 400 (Error in provided data) |

---

### 3.2 Obtención de Recursos  
**(Ejemplo: Fetch List of Places)**

Este flujo ilustra una operación de lectura, donde la **Business Logic** orquesta la consulta a la base de datos y crea la lista de objetos para retornar.

![Fetching List of Places](WhatsApp%20Image%202025-10-02%20at%2010.51.33%20AM.jpeg)

| Diagrama | Propósito | Código de Éxito | Código de Error |
|-----------|------------|----------------|----------------|
| WhatsApp Image 2025-10-02 at 10.51.33 AM.jpeg | Fetching List of Places | 201 (Return List of Places) | 404 (No place found) |

---

### Flujo de Datos Típico – Ejemplo: Crear un nuevo Place

El siguiente flujo muestra lo que ocurre cuando el cliente crea un nuevo alojamiento (`Place`), según el diagrama de secuencia:

1. **User → API:** Envía la petición `API call (create place)`.  
2. **API → Business Logic:** Realiza la validación de formato simple (`Validate simple data and process request`).  
3. **Business Logic → Persistence Layer:** Valida la lógica de negocio (`Validate data and request creation of Place`).  
4. **Persistence Layer → Database:** Si es válido, se invoca `Create and Save new Place`.  
5. **Retorno de Éxito:** La confirmación (`Confirm Save, Return Success`) viaja de vuelta, y la API responde al `User` con el código **201 Created**.

---

### Propósito del Diagrama

El diagrama de secuencia es vital porque:
- Muestra las interacciones dinámicas y el orden de los mensajes.  
- Clarifica que la validación y la lógica de negocio se ejecutan en la **Business Logic Layer**, mientras que la **I/O (Input/Output)** se maneja exclusivamente en la **Persistence Layer**.

---

## Conclusión

El diseño modular y la arquitectura en capas del proyecto **HBnB** permiten:
- Mantener un código limpio, organizado y escalable.  
- Separar claramente la presentación, la lógica y la persistencia.  
- Facilitar la evolución del sistema sin afectar otras partes del código.

En conjunto, esta **documentación técnica** define la base conceptual para la implementación del proyecto **HBnB** y sirve como **guía de referencia para el equipo de desarrollo**.
