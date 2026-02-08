```mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +API_endpoints
    +Service
}
class BusinessLogicLayer {
    +User
    +Place
    +Review
    +Amenity
}
class PersistenceLayer {
    <<Repository>>
    +Repositories
    +DatabaseAccessObjects
}
PresentationLayer --> BusinessLogicLayer : Use Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
