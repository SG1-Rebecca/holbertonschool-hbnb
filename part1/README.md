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

**2. Business Logic Layer (BLL)**

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

### Sequence Diagram

