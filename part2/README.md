# Part 2: Implementation of Business Logic and API Endpoints

## Project structure
```
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
|   |   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│   |   ├── __init__.py
│   |   ├── repository.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_user.py
│   │   ├── test_place.py
│   │   ├── test_review.py
│   │   ├── test_amenity.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

## Directory and file purpose

An empty `__init__.py` file is created in each directory that is intended to be a Python package.
This tells Python to treat these directories as importable packages.


- `app/` : Core application logic.

- `api/` : API endpoints, organized by version (v1/).

- `models/` : Business objects (User, Place, Review, Amenity) inheriting from `BaseModel`.

- `services/` : The Facade acting as the intermediary between the API and the Persistence layer.

- `persistence/` : In-memory repository.

- `tests/` : Unit and integration tests.

- `run.py`: The entry point for running the Flask application.
- `config.py`: Configuration of environment variables and application settings.
- `requirements.txt`: List all the Python packages needed for the project.

## Business Logic Layer

The Business Logic Layer handles the core functionality of the HBnB platform through four entities:

### 1. User

Represents a user of the platform, who can be either a property owner or a guest writing reviews.

**Responsibilities:**
- Store and manage personal information: `first_name`, `last_name`, `email`
- Manage the `is_admin` flag to distinguish between regular users and administrators
- Track associated places (properties owned by the user)
- Track reviews written by the user


### 2. Amenity

Represents a feature or service associated with a place (e.g., Wi-Fi, pool, gym, parking).

**Responsibilities:**
- Store the amenity name with proper validation
- Associate amenities with multiple places
- Ensure name is non-empty and within maximum length


### 3. Place

Represents a rental property available on the platform.

**Responsibilities:**
- Store property details: `title`, `description`, `price`, `latitude`, `longitude`
- Manage the relationship with the property owner (User)
- Track associated reviews and amenities
- Enforce data validation for all attributes


### 4. Review

Represents a review left by a user for a specific place, including a rating and commentary.

**Responsibilities:**
- Store review text and rating (1-5 stars)
- Associate the review with both a place and a user
- Ensure review text is non-empty and properly formatted
- Validate that rating is an integer between 1 and 5

**Business Rules:**
- Users cannot review their own properties
- Each user can only review a place once

## Setup I  nstructions

### 1. Clone and navigate

```bash
  git clone https://github.com/SG1-Rebecca/holbertonschool-hbnb.git
  cd holbertonschool-hbnb/part2/hbnb
```

### 2. Virtual environment

**2.1. Create an environment**

```bash
# Linux/MacOS
python3 -m venv .venv

# Windows
.venv\Scripts\activate
```

**2.2. Activate the environment**

```bash
# Linux/MacOS
. .venv/bin/activate

# Windows
venv\Scripts\activate  
```

### 3. Upgrade pip

```bash
pip install --upgrade pip
```

### 4. Install dependencies

```bash
  pip install -r requirements.txt
```

### 5. Run the application

```bash
  python run.py
```

## Running Tests (unittest)
- To run all tests from the project root:

```bash
python -m unittest discover -v
```

- To display the name of each test and its result
```bash
python3 -m unittest app.tests.test_filename -v
```