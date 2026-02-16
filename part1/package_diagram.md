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
    User
    Place
    Review
    Amenity
    end

    subgraph PersistenceLayer["Persistence Layer"]
    direction TB
    DatabaseAccess["Database Access"]
    Repositories
    Repositories --> DatabaseAccess
    end

PresentationLayer -- Use Facade Pattern --> BusinessLogicLayer
BusinessLogicLayer -- Database Operations--> PersistenceLayer
