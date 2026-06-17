Create/replace your `README.md` with this:

```markdown
# Containerized Project Management API

A production-style RESTful Project Management API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy ORM**, **JWT Authentication**, and **Docker Compose**.

This backend provides secure user authentication, project management, task tracking, database persistence, and automated testing.

---

## 🚀 Features

### Authentication & Security
- User registration
- Secure password hashing using bcrypt
- JWT based authentication
- Protected API routes
- User ownership authorization

### Project Management
- Create projects
- View user projects
- Get project details
- Update projects
- Delete projects

### Task Management
- Create tasks inside projects
- View project tasks
- Update task status
- Delete tasks
- Task ownership validation

### Database
- PostgreSQL database
- SQLAlchemy ORM
- Entity relationships
- Automatic table creation

### Architecture
- Layered architecture
- Repository pattern
- Service layer
- Dependency injection
- Input validation
- Error handling

### DevOps
- Dockerized application
- Docker Compose setup
- Environment configuration
- Persistent database storage

### Testing
- Unit tests
- Integration tests
- API endpoint testing

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend language |
| FastAPI | REST API Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Pydantic | Validation |
| JWT | Authentication |
| bcrypt | Password security |
| Docker | Containerization |
| Pytest | Testing |

---

# Project Structure

```

Containerized Project Management API

├── src
│   ├── api
│   │   ├── auth.py
│   │   ├── projects.py
│   │   └── tasks.py
│   │
│   ├── core
│   │   ├── security.py
│   │   └── exceptions.py
│   │
│   ├── database
│   │   ├── models.py
│   │   ├── database.py
│   │   └── repository.py
│   │
│   ├── services
│   │   ├── auth_service.py
│   │   ├── project_service.py
│   │   └── task_service.py
│   │
│   └── main.py
│
├── tests
│   ├── unit
│   │   ├── test_security.py
│   │   └── test_project_service.py
│   │
│   └── integration
│       ├── test_auth_api.py
│       └── test_project_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md

````

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd Containerized-Project-Management-API
````

---

# Environment Setup

Create `.env` file:

```env
DATABASE_URL=postgresql://user:password@db:5432/project_management_db

SECRET_KEY=supersecretkey

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Run Using Docker

Build and start containers:

```bash
docker compose up --build
```

The application will start:

API:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

PostgreSQL:

```
localhost:5432
```

---

# Stop Application

```bash
docker compose down
```

Remove database volume:

```bash
docker compose down -v
```

---

# API Documentation

## Authentication

### Register User

POST

```
/api/auth/register
```

Example:

```json
{
 "email":"user@gmail.com",
 "password":"123456"
}
```

Response:

```json
{
 "message":"User registered successfully"
}
```

---

## Login

POST

```
/api/auth/login
```

Response:

```json
{
 "access_token":"JWT_TOKEN",
 "token_type":"bearer"
}
```

---

# User API

## Current User

GET

```
/api/users/me
```

Header:

```
Authorization: Bearer TOKEN
```

---

# Project API

## Create Project

POST

```
/api/projects
```

Body:

```json
{
"name":"My Project",
"description":"Project description"
}
```

---

## Get Projects

GET

```
/api/projects
```

---

## Get Project

GET

```
/api/projects/{id}
```

---

## Update Project

PUT

```
/api/projects/{id}
```

---

## Delete Project

DELETE

```
/api/projects/{id}
```

---

# Task API

## Create Task

POST

```
/api/projects/{projectId}/tasks
```

Example:

```json
{
"title":"Build API",
"description":"Complete backend",
"status":"TODO"
}
```

---

## Get Tasks

GET

```
/api/projects/{projectId}/tasks
```

---

## Get Task

GET

```
/api/tasks/{id}
```

---

## Update Task

PUT

```
/api/tasks/{id}
```

---

## Delete Task

DELETE

```
/api/tasks/{id}
```

---

# Authentication Flow

1. Register account

2. Login

3. Receive JWT token

4. Add token to requests:

```
Authorization: Bearer <token>
```

5. Access protected resources

---

# Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Expected:

```
8 passed
```

---

# Error Handling

API returns proper HTTP responses:

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |
| 500  | Server Error |

---

# Database Models

## User

Fields:

* id
* email
* hashed_password
* active status

## Project

Fields:

* id
* name
* description
* owner_id

## Task

Fields:

* id
* title
* description
* status
* project_id

Relationships:

User → Projects

Project → Tasks

---

# Security

Implemented:

* bcrypt password hashing
* JWT authentication
* Protected endpoints
* Resource ownership checks
* Environment variables for secrets

---

# Development

Run locally:

```bash
uvicorn src.main:app --reload
```

---

# Author

Developed as a backend engineering project demonstrating:

* REST API design
* Authentication
* Database management
* Docker deployment
* Automated testing

