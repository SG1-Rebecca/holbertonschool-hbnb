# HBnB - UML
## Part 1: Technical Documentation
### High-Level Package Diagram

#### Layer Descriptions and Responsibilities
The application follows a 3-tier architecture, composed of the following layers:

**1. Presentation Layer**

**Description:**

The presentation layer serves as the interface between the user and the application. It encapsulates all user interactions, managing the representation of information and handling input from users.

**Responsibilities:**

- Handle HTTP requests and responses via API endpoints
- Validate incoming request payloads
- Format responses (JSON, etc...)
- Delegate business logic to the Business Logic Layer via Facade Pattern
- Manage error responses and user feedback

**2. Business Logic Layer**

**Description:**

The Business Logic Layer encapsulates the core logic of the application. It acts as an intermediary between the Presentation and Persistence layers, managing key entities (User, Place, Review, Amenity), enforcing business rules, and coordinating interactions between components.

**Responsibilities:**

- Manage entity lifecycle (creation, update, deletion)
- Enforce business rules and validate inputs
- Coordinate services and interactions between components
- Orchestrate complex workflows (e.g., creating a Place with associated Amenities and Reviews)
- Communicate with the Persistence Layer for data operations

**3. Persistence Layer**

**Description:**

The Persistence Layer is responsible for data storage, retrieval, and integrity. It abstracts the underlying database and provides a consistent interface for data access.

**Responsibilities:**

- Provide Repository interfaces and implementations (e.g., UserRepository, PlaceRepository)
- Execute database queries and manage transactions
- Map domain objects to database records and vice versa
- Ensure data consistency, integrity, and isolation
- Abstract database-specific details from the Business Logic Layer


### Class Diagram

BaseModel (Abstract Class)

Role: Serves as an abstract foundation for all entities, providing common attributes and methods to eliminate code duplication.

Key Attributes:

id: UUID4 - Universal unique identifier for each instance

created_at: DateTime - Creation timestamp for audit trails

updated_at: DateTime - Last modification timestamp

Methods: save(), create(), update(), delete()

to_dict() - Object serialization for API responses


**User**

Role: Represents the individuals using the application (e.g., guests, hosts).

Key Attributes: user_id, first_name, last_name, email, password.

Methods: .

Relationships: Links with the Place and Review entities to manage listings and feedback.

**Place**

__Role:__ Represents the properties available for booking (e.g., houses, apartments).

Key Attributes: place_id, title, description, price, latitude, longitude.

Methods:.

Relationships: Connected to User (creator) and Review (for user feedback).

**Review**

Role: Captures user feedback about a specific place.

Key Attributes: user_id, place_id, rating, comment.

Methods: list_by_place().

Relationships: Links back to User (review writer) and Place (the reviewed entity).

**Amenity**

Role: Represents additional features or services available at a place (e.g., pool, wifi).

Key Attributes: amenity_id, name, description.

Methods: list().

Relationships: Associated with Place to describe available amenities.

**Relationships between entities**

- User -> Place : One to Many
- Place -> Review: One to Many
- Place -> Amenity: Many to Many

### Sequence Diagram

