```mermaid
classDiagram
class BaseModel {
    - id: UUID4
    - created_at: Date
    - updated_at: Date
    + save ()
    + update ()
    + delete ()
    + to_dict() dict
    + validate()
}
class User {
    - first_name: string
    - last_name: string
    - email: string
    - password: string
    - is_admin: boolean
    - register()
}
class Place {
    - owner_id: UUID4
    - title: string
    - description: string
    - price: float
    - latitude: float
    - longitude: float
    + add_amenity()
}
class Review {
    - user_id: UUID4
    - place_id: UUID4
    - rating: int
    - comment: string
    + validate_rating()
    + validate_comment()
}
class Amenity {
    - name: string
    - description: string
}

BaseModel <|-- User
BaseModel <|-- Place
BaseModel <|-- Review
BaseModel <|-- Amenity

User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" *-- "0..*" Review: receives
Place "*" --> "*" Amenity: has
