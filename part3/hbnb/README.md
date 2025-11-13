
# HBnB - Auth & DB

Welcome to Part 3 of the HBnB Project, where you will extend the backend of the application by introducing user authentication, authorization, and database integration using SQLAlchemy and SQLite for development. Later, you’ll configure MySQL for production environments. In this part, you will secure the backend, introduce persistent storage, and prepare the application for a scalable, real-world deployment.

## Main Objectives

JWT Authentication using Flask-JWT-Extended

Role-based Authorization with an is_admin flag

Database Integration using SQLAlchemy with SQLite (and MySQL for production)

Full CRUD with Persistence instead of in-memory storage

Database Schema Design with Mermaid.js

## Project Structure

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
|   |       ├── auth.py
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
  cd holbertonschool-hbnb/part3/hbnb
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
```

### 6. Install dependencies

```python
  pip install -r requirements.txt
```

### 7. Run the application

```python
  python run.py
  # or
  flask run
```

