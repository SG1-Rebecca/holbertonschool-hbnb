```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Request a list of places
API->>BusinessLogic: Validate filter criteria

alt Valid filters criteria
    BusinessLogic->>Database: Fetch filtered places
    Database-->>BusinessLogic: Return places list
    BusinessLogic-->>API: Return Place data
    API-->>User: Return Success (places list)

else Invalid filters criteria
    BusinessLogic-->>API: Return response
    API-->>User: Return Failure
end