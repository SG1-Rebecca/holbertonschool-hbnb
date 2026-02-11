```mermaid
classDiagram
class Base Model {
    - id: 
    - create_at: Date
    - update_at: Date
}
class User {
    - first_name: string
    - last_name: string
    - email: string
    - password: string
    +MethodType methodName()
}
class Place {
    - title: string
    - description: string
    - price:
    - latitude:
    - longitude:
    +MethodType methodName()
}
class Review {
    - rating: int
    - comment: string
    +MethodType methodName()
}
class Amenity {
    - name: string
    - description: string
    +MethodType methodName()
}
BaseModel --|> User
BaseModel --|> Place
BaseModel --|> Review
BaseModel --|> Amenity
Place --* Review: has
User --> Place : owns
User --> Review : writes
