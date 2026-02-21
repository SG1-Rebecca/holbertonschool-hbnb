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
python -m unittest discover
```

- To display the name of each test and its result
```bash
python3 -m unittest -v tests/filename
```