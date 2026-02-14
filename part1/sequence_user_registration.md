```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Register User (user data)
API->>BusinessLogic: Validate and Process Request

alt Invalid data
    BusinessLogic-->>API: Return Response
    API-->>User: Return Failure

else Valid data
    BusinessLogic->>Database: Check if user exists
    Database-->>BusinessLogic: User exists / Not found

    alt User already exists
        BusinessLogic-->>API: Return Response
        API-->>User: Return Failure
    
    else User does not exist
        BusinessLogic->>Database: Save data
        Database-->>BusinessLogic: Confirm save
        BusinessLogic-->>API: Return Response
        API-->>User: Return Success
    end
end
