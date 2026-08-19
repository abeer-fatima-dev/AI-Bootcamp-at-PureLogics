# My first Flask API

## Overview

My first Flask API is a RESTful web application developed using **Flask** as part of the AI Bootcamp at PureLogics. The project demonstrates the fundamental concepts of backend API development by implementing complete CRUD (Create, Read, Update, Delete) operations using an in-memory data store.

This project serves as a practical introduction to building REST APIs with Flask while following a simple, modular, and maintainable project structure. The API is designed to be tested using **Postman** and can easily be extended to support database integration and authentication in future versions.

---

## Project Objectives

This project was developed to:

- Understand the fundamentals of RESTful API development.
- Learn Flask application architecture.
- Implement CRUD operations using HTTP methods.
- Handle JSON requests and responses.
- Build and test APIs using Postman.
- Practice organizing backend projects.
- Strengthen backend development skills using Python.

---

## Features

- Home endpoint
- About endpoint
- Retrieve all tasks
- Retrieve a task by ID
- Create a new task
- Update an existing task
- Delete a task
- JSON request and response handling
- Error handling for invalid requests
- Modular project organization

---

## Project Structure

```text
My First Flask API/
│
├── app.py
├── storage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3.10+
- Flask
- Postman
- JSON
- Git
- GitHub

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/abeer-fatima-dev/AI-Bootcamp-at-PureLogics.git
```

### Navigate to the Project

```bash
cd "My First Flask API"
```

### Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask development server.

```bash
python app.py
```

The application will start on:

```
http://127.0.0.1:5000
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|-----------------|------------------------------|
| GET | `/` | Home endpoint |
| GET | `/about` | About the application |
| GET | `/todos` | Retrieve all tasks |
| GET | `/todos/<id>` | Retrieve a task by ID |
| POST | `/todos` | Create a new task |
| PUT | `/todos/<id>` | Update an existing task |
| DELETE | `/todos/<id>` | Delete an existing task |

---

## Request Example

### Create Task

**POST** `/todos`

```json
{
    "task": "Complete Flask Assignment"
}
```

---

### Update Task

**PUT** `/todos/1`

```json
{
    "task": "Learn Flask API Completely"
}
```

---

## Sample Response

```json
{
    "message": "Task added successfully",
    "todo": {
        "id": 1,
        "task": "Complete Flask Assignment"
    }
}
```

---

## Testing

The API was tested using **Postman**.

The following operations were successfully verified:

- Retrieve all tasks
- Retrieve a task by ID
- Create a new task
- Update an existing task
- Delete a task
- Error handling for invalid IDs

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- REST API Development
- Flask Framework
- CRUD Operations
- HTTP Methods (GET, POST, PUT, DELETE)
- JSON Request and Response Handling
- Backend Application Development
- API Testing with Postman
- Git and GitHub Version Control
- Modular Project Organization

---

## Future Enhancements

This project can be extended by implementing:

- SQLite or PostgreSQL database integration
- SQLAlchemy ORM
- User Authentication using JWT
- Password Hashing
- User Registration and Login
- Input Validation
- Logging
- Docker Containerization
- Automated Testing with Pytest
- Deployment on Render or Railway
- Machine Learning Model Integration
- API Documentation using Swagger (Flasgger)

---

## Author

**Abeer Fatima**

AI Bootcamp — PureLogics

GitHub: https://github.com/abeer-fatima-dev

---

## License

This project was developed for educational purposes as part of the AI Bootcamp at PureLogics. It is intended for learning backend development using the Flask framework.
