
# HBnB - Authentication & DataBase

Lorem ipsum

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
│   |   ├── __init__.py
│   |   ├── repository.py
│   ├── test/
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


## Instructions

### 1. Clone the project

```bash
  git clone https://github.com/SG1-Rebecca/holbertonschool-hbnb.git
```

### 2. Go to the project directory

```bash
  cd holbertonschool-hbnb/part3/hbnb
```

### 3. Create a virtual environment
**On Linux/Mac:**

```python
python3 -m venv .venv
```

**On Windows:**

```python
.venv\Scripts\activate
```

### 4. Activate the virtual environment

```python
. .venv/bin/activate
```

### 5. Upgrade pip

```python
pip install --upgrade pip
```

### 6. Install dependencies

```python
  pip install -r requirements.txt
```

### 7. Run the application

```python
  python run.py
```

## Testing with unittest
To run all tests from the project root:

```python3
python -m unittest discover
```

