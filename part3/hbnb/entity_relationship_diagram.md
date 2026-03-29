```mermaid
erDiagram
    USER ||--o{ PLACE : owns
    USER ||--o{ REVIEW : writes
    USER ||--o{ RESERVATION : makes
    PLACE ||--o{ REVIEW : receives
    PLACE ||--O{ RESERVATION : books
    PLACE ||--o{ PLACE_AMENITY : includes
    AMENITY ||--o{ PLACE_AMENITY : includes

    USER {
        string id PK
        string first_name
        string last_name
        string email
        string password
        bool is_admin
    }

    PLACE {
        string id PK
        string title
        text description
        float price
        float latitude
        float longitude
        string owner_id FK
    }

    REVIEW {
        string id PK
        string text
        integer rating
        string user_id FK
        string place_id FK
    }

    AMENITY {
        string id PK
        string name
    }

    PLACE_AMENITY {
        string place_id FK
        string amenity_id FK
    }

    RESERVATION {
        string id PK
        date start_date
        date end_date
        integer guests
        string user_id FK
        string place_id FK
    }
