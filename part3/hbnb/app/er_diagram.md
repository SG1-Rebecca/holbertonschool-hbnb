```mermaid
erDiagram
    USER ||--o{ PLACE : Owns
    USER ||--o{ REVIEW : Writes
    PLACE ||--o{ REVIEW : Receives
    PLACE ||--o{ PLACE_AMENITY : has
    AMENITY ||--o{ PLACE_AMENITY : a