```mermaid
flowchart TD
    subgraph PresentationLayer["Presentation Layer"]
    direction TB
    API_endpoints[API Endpoints]
    Services
    API_endpoints --> Services
    end

    subgraph BusinessLogicLayer["Business Logic Layer"]
    direction TB
    Models
    User
    Place
    Review
    Amenity
    end

    subgraph PersistenceLayer["Persistence Layer"]
    DatabaseAccess["Database Access"]
    end

PresentationLayer -- Use Facade Pattern --> BusinessLogicLayer
BusinessLogicLayer -- Database Operations--> PersistenceLayer
