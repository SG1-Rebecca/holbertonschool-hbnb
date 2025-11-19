```mermaid
erDiagram
    direction LR
    USER ||--o{ PLACE : owns
    USER ||--o{ REVIEW : writes
    PLACE ||--o{ REVIEW : receives
    PLACE ||--o{ PLACE_AMENITY : has
    AMENITY ||--o{ PLACE_AMENITY : Is_part_of
    USER{
        char id PK
        string first_name
        string last_name
        string email
        string password
        bool is_admin
    }
    PLACE{
        char id PK
        string title
        text description
        decimal price
        float latitude
        float longitude
        char owner_id FK
    }
    REVIEW{
        char id PK
        text text
        int rating
        char user_id FK 
        char place_id FK 
    }
    AMENITY{
        char id PK
        string name
    }
    PLACE_AMENITY{
        char place_id FK
        char amenity_id FK
    }