# My first Fast API App

## Overview

The **My first Fast API App ** is a RESTful application developed using **FastAPI** as part of the AI Bootcamp at PureLogics. The project demonstrates the fundamentals of backend API development by implementing CRUD (Create, Read, Update, and Delete) operations while following a clean and modular project structure.

The application exposes REST endpoints that can be tested using both Swagger UI and Postman, making it suitable for learning API development and backend architecture.

---

## Objectives

The primary objectives of this project are to:

- Understand REST API development using FastAPI.
- Implement CRUD operations.
- Learn request validation using Pydantic.
- Organize a project following modular architecture.
- Test APIs using Swagger UI and Postman.
- Build a maintainable backend application.

---

## Features

- Home endpoint
- About endpoint
- Retrieve all records
- Retrieve a record by ID
- Create new records
- Update existing records
- Delete records
- Automatic interactive API documentation
- Request validation using Pydantic
- JSON request and response handling

---

## Project Structure

```text
Student-Performance-Prediction-App/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── storage.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI
- Postman

---

## Installation

### Clone the repository

```bash
git clone https://github.com/abeer-fatima-dev/AI-Bootcamp-at-PureLogics.git
```

### Navigate to the project directory

```bash
cd Student-Performance-Prediction-App
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the development server using Uvicorn.

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|-----------------|------------------------------|
| GET | `/` | Home endpoint |
| GET | `/about` | About the application |
| GET | `/todos` | Retrieve all records |
| GET | `/todos/{id}` | Retrieve a record by ID |
| POST | `/todos` | Create a new record |
| PUT | `/todos/{id}` | Update an existing record |
| DELETE | `/todos/{id}` | Delete a record |

---

## Testing

The API can be tested using:

- Swagger UI
- Postman

---

## Learning Outcomes

This project provided practical experience in:

- REST API development
- FastAPI framework
- Backend application architecture
- CRUD implementation
- Request validation
- API testing
- Project organization
- Version control using Git and GitHub

---

## Future Improvements

The following enhancements can be added in future iterations:

- Database integration (SQLite or PostgreSQL)
- JWT Authentication
- User management
- Environment configuration
- Docker containerization
- Automated testing using Pytest
- Logging and monitoring
- Machine Learning model integration

---

## Author

**Abeer Fatima**

AI Bootcamp — PureLogics

GitHub: https://github.com/abeer-fatima-dev

---

## License

This project is intended for educational purposes as part of the AI Bootcamp at PureLogics.
