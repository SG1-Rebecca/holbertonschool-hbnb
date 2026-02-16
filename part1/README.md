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

**Role:** Represents the properties available for booking (e.g., houses, apartments).

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

### 3.Sequence Diagram

### 3.1 User registration

**1. Initialization**

**User -> API:** Register User (user data)
The client submits registration information (first_name, last_name, email, password) to the system's entry point.

**API -> BusinessLogic:** Validate and Process Request
The API delegates the request to the business logic layer, separating HTTP concerns from core processing.

**2. First Check - Data Validation**

BusinessLogic performs validation

The business layer checks for:

-> Correct data formats (valid email, password strength)

-> Required fields presence

-> Business-specific rules

**3. Conditional Flow A: Invalid Data**

- **BusinessLogic --> API:** Return validation failure response with error details

- **API --> User:** Return Failure
User receives error message about what needs correction

**4. Conditional B: Valid Data → Existence Check**

- **BusinessLogic -> Database:** Check if user exists
queries database using unique identifiers (typically email)

- **Database --> BusinessLogic:** User exists / Not found
Returns existence status

**5. Conditional B1: User Already Exists**

- **BusinessLogic --> API:** Return Failure response "user already registered" error

- **API --> User:** Return Failure
User informed of duplicate registration attempt

**6. Conditional B2: User Does Not Exist → Registration**

- **BusinessLogic -> Database:** Save data
Creates new user record

- **Database --> BusinessLogic:** Confirm save
Returns success confirmation with user ID

- **BusinessLogic --> API:** Returns success response with user details

- **API --> User:** Return Success
User receives confirmation of successful registration

### 3.2 Place Creation

**1. Initialization**

**User -> API:** Place Creation (place data)
The user submits place information (title, description, price, coordinate, amenities, etc.) to create a new listing

**API -> BusinessLogic:** Validate and Process Request
The API forwards the place data to the business logic layer for processing

**2. First Check - Data Validation**

BusinessLogic performs validation on the place data:

-> Required fields: title, description, price, latitude, longitude

-> Price must be a positive number

-> Coordinate format validation

-> Owner information must be valid

**3. Conditional Flow A: Invalid Data**

- **BusinessLogic --> API:** Return Failure response validation error details (e.g., "Price must be greater than 0", "Coordinate required")

- **API --> User:** Return Failure
User receives specific error messages for correction

**4. Conditional Flow B: Valid Data →  Duplicate Check**

- **BusinessLogic -> Database:** Check if Place exists
Queries database to check if the same owner already has a similar/identical place listing

- **Database --> BusinessLogic:** Place Status
Returns whether a matching place exists for this owner

**5. Conditional Flow B1: Duplicate Place**

- **BusinessLogic --> API:** Return Failure response
"duplicate place" error - the owner cannot create a duplicate listing

- **API --> User:** Return Failure (Duplicated place)
User informed that they cannot create a duplicate listing

**6. Conditional Flow B2: Place Does Not Exist → Creation**

- **BusinessLogic -> Database:** Save Place data
Creates new place record with all provided information

- **Database --> BusinessLogic:** Confirm Save
Returns success confirmation with new place ID and timestamp

- **BusinessLogic --> API:** Returns success response with place details (ID, creation date, etc.)

- **API --> User:** Return Success (place created)
User receives confirmation that his Place created successfully