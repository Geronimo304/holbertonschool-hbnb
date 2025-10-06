# HBnB Project Technical Documentation

## AirBnB Clone: A Platform for Accommodation Management
**Authors:** Sofia Nunez, Martin Suarez, Geronimo Negreira – #C27

---

## Introduction

This document serves as the detailed blueprint and technical reference for the development of the **HBnB** project (a simplified AirBnB clone).  
Its objective is to consolidate the architectural diagrams, business logic design, and API interaction flows, in order to guide the implementation and ensure that all developers have a clear and unified understanding of the system.

---

## 1. High-Level Architecture

This section presents an overview of the application, showing how the main components are organized.

### High-Level Package Diagram

The following diagram illustrates the three-layer architecture and how the **Facade** acts as the contact point between the **Presentation** and the **Business Logic**.

![High-Level Package Diagram](WhatsApp%20Image%202025-10-02%20at%2010.51.18%20AM.jpeg)

---

### Architecture Explanation

The **HBnB** project follows a **Layered Architecture** to separate responsibilities, which makes the code more manageable, modular, and scalable.

#### Presentation Layer / API (Presentation Layer)
- Contains the services (+ ServiceAPI) and endpoints that handle user requests.  
- It contains no business logic; its role is to receive the request, pre-validate it (format), and pass it to the lower layer.

#### Facade Layer (Facade)
- The "Facade Pattern" link indicates that the Presentation Layer uses a design pattern that simplifies access to the business logic, offering a unified interface and decoupling the two layers.

#### Business Logic Layer (Business Logic Layer)
- The core of the application.  
- Contains the main system classes (+ Place, + User, + Review, + Amenity) and the business rules.  
- Defines how the system entities behave and relate to each other.

#### Persistence Layer (Persistence Layer)
- Contains the database access (+ DatabaseAccess).  
- It is the only layer that interacts directly with the database.

---

### Design Rationale

This layer separation is crucial because:
- It allows each layer to be developed, tested, and maintained in isolation.  
- It improves the system's modularity, reusability, and robustness.  
- It facilitates the incorporation of new technologies (like a new type of database) without breaking the rest of the architecture.

---

## 2. Business Logic Layer

This layer defines the system entities, their attributes, methods, and their relationships.

### Detailed Class Diagram

The diagram below is the visual representation of the core business logic of **HBnB**, including the entities, their attributes, and their relationships with multiplicity (e.g., 1..*).

![Detailed Class Diagram](WhatsApp%20Image%202025-10-03%20at%203.27.22%20PM.jpeg)

---

### Data Model Explanation

The class diagram shows the main entities (Models) that define the project and their relationships.  
All key classes (**Place**, **Review**, **Amenity**) inherit from the common base class **Base**, which provides the object's identity structure.

#### Main System Classes

**Base:** Provides the essential tracking attributes:  
- +str uid (Unique UUID, which acts as the id).  
- +int up (Represents timestamps like created\_at or updated\_at).

**User:** Represents a user or host.  
- Attributes: `name`, `lastname`, `age`, `password`.  
- Business Methods: `+postPlace(place: Places)`, `+bookPlace(place: Places)`, `+makeReview(review: Review, place: Places)`.  
- Relationship: `1 owns 0..* Place`, `1 writes 0..* Review`.

**Place:** The accommodation offered.  
- Attributes: `coordinates (tuple)`, `description`, `amenities (list)`, `price`, `owner (User)`.  
- Business Method: `+addAmenity(amenity: Amenity)`.  
- Relationship: `1 has 0..* Amenity`, `1 receives 0..* Review`.

**Review:** A review of a `Place` by a `User`.  
- Attributes: `rating (int)`, `comment (str)`, `reviewer (User)`, `place (Place)`.

**Amenity:** Represents the available services (`list name`).

---

### Design Decisions

- **Base Inheritance:** The use of the `Base` class ensures that the business classes (`Place`, `Review`, `Amenity`) share fundamental fields for persistence (like the `uid`), maintaining model coherence.  

- **Clear Relationships:** Multiplicity ensures data integrity; for example, a `Place` must be owned by exactly one `User` (`1 owns 0..* Place`).

---

## 3. API Interaction Flow

This section illustrates how data requests flow between the different system components when interacting with the API.

### Sequence Diagrams for API Calls

The diagrams detail the sequence of events (messages) between the actors (`User`) and the subsystems (`API`, `Business Logic`, `Persistence Layer`, `Database`) to fulfill a request.

---

### 3.1 Resource Creation  
**(Examples: Register User, Create Place, Submit Review)** This generic flow, which culminates in the **HTTP 201 (Created)** code, illustrates multi-layer validation before persistence.

| Diagram | Purpose | Success Code | Error Code |
|-----------|------------|----------------|----------------|
| ![User Registration](WhatsApp%20Image%202025-10-02%20at%2010.51.34%20AM%20(1).jpeg) | User Registration | 201 | 400 (Error in provided data) |
| ![Place Creation](WhatsApp%20Image%202025-10-02%20at%2010.51.34%20AM.jpeg) | Place Creation | 201 | 400 (Error in provided data) |
| ![Review Submission](WhatsApp%20Image%202025-10-02%20at%2010.51.33%20AM%20(1).jpeg) | Review Submission | 201 | 400 (Error in provided data) |

---

### 3.2 Resource Retrieval  
**(Example: Fetch List of Places)**

This flow illustrates a read operation, where the **Business Logic** orchestrates the query to the database and creates the list of objects to return.

| Diagram | Purpose | Success Code | Error Code |
|-----------|------------|----------------|----------------|
| ![Fetching List of Places](WhatsApp%20Image%202025-10-02%20at%2010.51.33%20AM.jpeg) | Fetching List of Places | 201 (Return List of Places) | 404 (No place found) |

---

### Typical Data Flow – Example: Create a New Place

The following flow shows what happens when the client creates a new accommodation (`Place`), according to the sequence diagram:

1. **User → API:** Sends the request `API call (create place)`.  
2. **API → Business Logic:** Performs simple format validation (`Validate simple data and process request`).  
3. **Business Logic → Persistence Layer:** Validates the business logic (`Validate data and request creation of Place`).  
4. **Persistence Layer → Database:** If valid, `Create and Save new Place` is invoked.  
5. **Success Return:** The confirmation (`Confirm Save, Return Success`) travels back, and the API responds to the `User` with the code **201 Created**.

---

### Purpose of the Diagram

The sequence diagram is vital because:
- It shows the dynamic interactions and the order of messages.  
- It clarifies that validation and business logic are executed in the **Business Logic Layer**, while **I/O (Input/Output)** is handled exclusively in the **Persistence Layer**.

---
