Documentación Técnica del Proyecto HBnB
Clon de AirBnB: Una Plataforma para la Gestión de Alojamientos
Este documento sirve como el plan detallado y la referencia técnica para el desarrollo del proyecto HBnB (un clon simplificado de AirBnB). Su objetivo es consolidar los diagramas de arquitectura, el diseño de la lógica de negocio y los flujos de interacción de la API para guiar la implementación y asegurar que todos los desarrolladores tengan una comprensión clara y unificada del sistema.

1. Arquitectura de Alto Nivel
Esta sección presenta la vista general de la aplicación, mostrando cómo se organizan los principales componentes.

Diagrama de Paquetes de Alto Nivel
[Aquí debes insertar la imagen del High-Level Package Diagram (Diagrama de Paquetes de Alto Nivel) de la Tarea 1]

Explicación de la Arquitectura
El proyecto HBnB sigue una Arquitectura de Capas (Layered Architecture) para separar responsabilidades, lo que hace que el código sea más manejable y escalable.

Capa de Presentación/Front-end (Web App / CLI): Esta capa se encarga de la interfaz de usuario, ya sea la aplicación web o la consola de comandos (CLI). Su única tarea es interactuar con el usuario y enviar peticiones a la capa inferior. No contiene lógica de negocio.

Capa de Fachada (Facade): Implementamos un Patrón Fachada. Este componente es el único punto de acceso a la lógica de negocio. Recibe las peticiones de la capa de presentación (ej. una petición HTTP de la API) y las dirige a la clase de lógica de negocio adecuada, simplificando la interfaz para la capa superior.

Capa de Lógica de Negocio (Business Logic Layer): Aquí reside el corazón de la aplicación. Contiene las clases de las entidades del proyecto (Usuario, Lugar, Ciudad, etc.) y las reglas que definen cómo se comportan y se relacionan.

Capa de Persistencia (Data Persistence Layer): Esta capa se encarga de almacenar y recuperar los datos. Se diseñó para ser independiente del resto del sistema, lo que nos permite cambiar fácilmente la tecnología de almacenamiento (de un sistema de archivos a una base de datos MySQL o PostgreSQL, por ejemplo) sin afectar la lógica de negocio.

Racional del Diseño: Esta separación es crucial. Permite que cada capa se desarrolle, pruebe y modifique de forma aislada, mejorando la modularidad y la robustez del sistema.

2. Capa de Lógica de Negocio
Esta capa define las entidades de nuestro sistema y sus relaciones.

Diagrama de Clases Detallado
[Aquí debes insertar la imagen del Detailed Class Diagram for the Business Logic Layer (Diagrama de Clases Detallado de la Lógica de Negocio) de la Tarea 2]

Explicación del Modelo de Datos
El diagrama de clases muestra las principales entidades (Modelos) que definen el proyecto y sus relaciones, todas heredando de una clase BaseModel para garantizar atributos comunes:

BaseModel: Clase base que provee atributos esenciales como id (UUID único), created_at y updated_at. Todas las demás clases la heredan.

User: Representa a un usuario o anfitrión. Se relaciona con Place (un usuario puede tener muchos lugares) y con Review (un usuario puede escribir muchas reseñas).

Place: El alojamiento en sí (como un apartamento o una casa). Es la entidad central. Se relaciona con un User (el anfitrión), una City y múltiples Amenity a través de relaciones de muchos a muchos o de uno a muchos.

City y State: Definen la ubicación de los alojamientos. La relación es jerárquica: un State contiene muchas City.

Review: Una reseña de un usuario sobre un Place.

Amenity: Representa servicios ofrecidos en el Place (ej. piscina, Wi-Fi).

Decisiones de Diseño: Al centralizar la lógica en esta capa, garantizamos que las reglas de negocio (como la validación de datos o la gestión de relaciones) se apliquen de manera consistente, sin importar si la petición viene de la web, de la API, o de la consola. Por ejemplo, solo un User puede ser el anfitrión de un Place.

3. Flujo de Interacción de la API
Esta sección ilustra cómo fluyen las peticiones de datos entre los diferentes componentes del sistema al interactuar con la API.

Diagramas de Secuencia para Llamadas API
[Aquí debes insertar las imágenes de los Sequence Diagrams for API Calls (Diagramas de Secuencia para Llamadas API) de la Tarea 3. Idealmente, uno para "Crear un objeto" y otro para "Obtener un objeto".]

Flujo de Datos Típico (Ej. Crear un nuevo Place)
El diagrama de secuencia detalla el flujo de una petición API para crear una nueva instancia (Place).

Client (Navegador/App): Inicia la petición HTTP (ej. POST /places) con los datos del nuevo lugar.

API Layer (Controlador/Ruta): Recibe la petición, valida el formato básico de la entrada y extrae los datos JSON.

Facade Layer (Fachada): Llama al método apropiado de la lógica de negocio (ej. Place.create_place(data)).

Business Logic Layer (Modelo Place):

Crea una instancia de la clase Place.

Aplica las reglas de negocio (ej. verifica que el anfitrión (user_id) exista, valida el precio, etc.).

Si es válido, serializa el objeto.

Llama al Persistence Layer para guardar el objeto (ej. Storage.save(new_place)).

Persistence Layer: Se comunica con el almacenamiento (archivo o DB) para guardar los datos. Devuelve la confirmación.

Retorno: El control se devuelve a la API Layer, que construye la respuesta HTTP (ej. código 201 Creado con el objeto Place en el cuerpo de la respuesta) y la envía de vuelta al Client.

Propósito del Diagrama: Muestra las interacciones dinámicas y la delegación de responsabilidades a lo largo de las capas. Es crucial para el desarrollo de la API porque define exactamente qué componente hace qué, asegurando una comunicación eficiente y sin cuellos de botella.
