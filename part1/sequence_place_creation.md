```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Place Creation (place data)
API->>BusinessLogic: Validate and Process Request

alt Invalid data
    BusinessLogic-->>API: Return Response
    API-->>User: Return Failure

else Valid data
    BusinessLogic->>Database: Check if Place exists
    Database-->>BusinessLogic: Place Status
    
    alt Place already exists for this owner
        BusinessLogic-->>API: Return Response
        API-->>User: Return Failure (Duplicated place)
        
    else Place does not exist
        BusinessLogic->>Database: Save Place data
        Database-->>BusinessLogic: Confirm Save
        BusinessLogic-->>API: Return Response
        API-->>User: Return Success (place created)
    end
end