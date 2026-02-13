```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Register User (user data)
API->>BusinessLogic: Validate and Process Request

alt Valid data
    BusinessLogic->>Database: Save Data
    Database-->>BusinessLogic: Confirm Save
    BusinessLogic-->>API: Success Response
    API-->>User: 201 Created

else Invalid data
    BusinessLogic-->>API: Validation Error
    API-->>User: 400 Bad Request (error details)
end

%% TODO user already exist