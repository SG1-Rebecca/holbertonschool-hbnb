
# HBnB - Business Logic & API 

This project implements the Business Logic Layer and RESTful API of the HBnB platform, building upon the system architecture defined in the UML diagram from Part 1.

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
  git clone https://github.com/SG1-Rebecca/holbertonschool-hbnb.git
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
pip install Flask flask-restx
```

### 6. Install dependencies

```python
  pip install -r requirements.txt
```

### 7. Run the application

```python
  python run.py
```

