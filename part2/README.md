
# HBnB - Business Logic & API 

This project

## Structure

```plaintext
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
## Instructions

### 1. Clone the project

```bash
  git clone https://github.com/ValentinDLC/holbertonschool-hbnb.git
```

### 2. Go to the project directory

```bash
  cd holbertonschool-hbnb/part2/hbnb
```
### 3. Create a virtual environment


```python
python3 -m venv .venv
```

### 4. Activate the virtual environment

```python
. .venv/bin/activate
```

### 5. Upgrade pip and Install Flask

```python
pip install --upgrade pip
pip install Flask
pip install flask-restx
```

### 6. Install dependencies

```python
  pip install -r requirements.txt
```

### 7. Run the application

```python
  python run.py
```

## Business Logic Layer

### Entities and their responsibilities

1. **User** : Represents a user of the platform (owner or tenant).

    **Responsibilities:**

    - Name validation
    - Email format validation
    - Ensuring email uniqueness
    - Linking with created places and reviews


2. **Place** : Represents a place available to rental

    **Responsibilities:**

    - Text Validation
    - Rating Validation
    - Living Space Validation
    - Validate user ownership
    - Business Rules
    - Timestamp Management


3. **Review** : Represents a review left by a user on a Place.

    **Responsabilities:**

    - Validating the rating
    - Verifying the existence of the user and the property
    - Prevent a property owner from rating their own property
    - Timestamp Management



4. **Amenity** : Represents a feature or service associated with one or more places

    **Responsibilities:**

    - Validate name.
    - Manage many-to-many associations with places.
    - Timestamp Management


## Relationships Between Entities


User <-> Place : One-To-Many

User <-> Review : One-To-Many

Place <-> Review : One-To-Many

Place <-> Amenity : Many-To-Many