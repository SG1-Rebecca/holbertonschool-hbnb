```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Submit Review (review data)
API->>BusinessLogic: Validate and create a review

alt User is the owner
    BusinessLogic-->>API: Return response
    API-->>User: Return Failure (cannot review own place)

else User is not the owner
    BusinessLogic->>Database: Save Place review in Database
    Database-->>BusinessLogic: Confirm Save
    BusinessLogic-->>API: Return response
    API-->>User: Return Success (review submitted)
end
