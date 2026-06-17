# Architecture Overview

## Project: Containerized Project Management API

This project follows a layered architecture using FastAPI, SQLAlchemy ORM, PostgreSQL, and Docker.

## Architecture Layers

```

Client (Postman / Frontend)
|
v
API Layer (FastAPI Routes)
|
v
Service Layer (Business Logic)
|
v
Repository Layer (Database Operations)
|
v
Database Layer (PostgreSQL + SQLAlchemy ORM)

```

## Components

### API Layer
- Handles HTTP requests and responses
- Provides RESTful endpoints
- Performs request validation using Pydantic
- Manages authentication dependencies

### Service Layer
- Contains application business logic
- Handles user registration, login, project and task operations
- Separates logic from API and database code

### Repository Layer
- Implements Repository Pattern
- Encapsulates database queries
- Provides CRUD operations for:
  - Users
  - Projects
  - Tasks

### Database Layer
- PostgreSQL used for persistent storage
- SQLAlchemy ORM manages database models
- Relationships:
  - One User → Many Projects
  - One Project → Many Tasks

## Authentication Flow

1. User registers with email and password
2. Password is encrypted using bcrypt
3. User logs in
4. Server generates JWT token
5. Token is required for protected APIs

## Containerization

Docker Compose manages:

- FastAPI application container
- PostgreSQL database container

Both services communicate through Docker networking.

## Testing

- Unit tests verify service logic
- Integration tests verify complete API flow
- Authentication and CRUD endpoints are tested

## Security

- JWT based authentication
- Password hashing
- Input validation
- Protected resources based on ownership
