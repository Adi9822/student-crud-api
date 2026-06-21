# Student CRUD REST API

## Overview

Student CRUD REST API is a backend application built using **Python, Flask, PostgreSQL, SQLAlchemy ORM, Docker, Docker Compose, and GNU Make**.

The project provides REST endpoints to create, retrieve, update, and delete student records while following backend development and DevOps best practices.

---

# Features

* Create Student
* Get All Students
* Get Student By ID
* Update Student
* Delete Student
* Health Check Endpoint
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Database Migrations using Flask-Migrate
* Environment Variable Configuration
* Logging
* Unit Testing using Pytest
* Docker Containerization
* Multi-stage Docker Build
* Docker Compose for Multi-Container Setup
* One-Click Local Development using Makefile

---

# Tech Stack

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python         | Programming Language       |
| Flask          | REST API Framework         |
| PostgreSQL     | Relational Database        |
| SQLAlchemy     | ORM                        |
| Flask-Migrate  | Database Migrations        |
| Pytest         | Unit Testing               |
| Docker         | Containerization           |
| Docker Compose | Multi-Container Management |
| GNU Make       | Task Automation            |

---

# Project Structure

```text
student-api/

├── app/
│   ├── config/
│   ├── models/
│   ├── routes/
│   └── __init__.py
│
├── migrations/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── .dockerignore
├── requirements.txt
├── run.py
├── README.md
└── .env
```

---

# Prerequisites

Before running the project, make sure the following tools are installed:

* Docker Desktop
* Docker Compose
* Python 3.x
* Git
* GNU Make (optional for Windows)

Verify installations:

```bash
docker --version
docker compose version
python --version
git --version
```

---

# Setup

## Clone Repository

```bash
git clone <repository-url>

cd student-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=studentdb
DB_USER=postgres
DB_PASSWORD=<your-db-password>
```

---

# Database Migration

Apply database migrations:

```bash
flask --app run.py db upgrade
```

---

# Local Development

## Start PostgreSQL Container

```bash
make start-db
```

---

## Run Database Migrations

```bash
make migrate
```

---

## Build REST API Docker Image

```bash
make build-api
```

---

## Run REST API

```bash
make run-api
```

---

# Execution Order

Running

```bash
make run-api
```

performs the following steps automatically:

```text
make run-api
        │
        ▼
start-db
        │
        ▼
migrate
        │
        ▼
build-api
        │
        ▼
docker compose up -d
```

This provides a one-click local development setup.

---

# Run Application (Without Docker)

```bash
python run.py
```

Application URL:

```text
http://localhost:5000
```

---

# API Endpoints

## Health Check

```
GET /healthcheck
```

Response

```json
{
    "status": "UP"
}
```

---

## Create Student

```
POST /api/v1/students
```

Request

```json
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 22
}
```

Response

```json
{
    "message": "Student created successfully",
    "id": 1
}
```

---

## Get All Students

```
GET /api/v1/students
```

---

## Get Student By ID

```
GET /api/v1/students/<id>
```

Example

```
GET /api/v1/students/1
```

---

## Update Student

```
PUT /api/v1/students/<id>
```

Example Request

```json
{
    "name": "Rahul Sharma",
    "age": 23
}
```

---

## Delete Student

```
DELETE /api/v1/students/<id>
```

---

# Running Tests

Execute unit tests:

```bash
pytest
```

Expected Output:

```text
2 passed
```

---

# Docker

## Build Docker Image

```bash
docker build -t student-api:1.0.0 .
```

---

## Start Services

```bash
docker compose up -d
```

---

## Stop Services

```bash
docker compose down
```

---

## View Running Containers

```bash
docker ps
```

---

## Verify API

```bash
curl http://localhost:5000/healthcheck
```

Expected Response

```json
{
    "status": "UP"
}
```

---

# Makefile Commands

| Command        | Description                  |
| -------------- | ---------------------------- |
| make install   | Install project dependencies |
| make run       | Run Flask application        |
| make test      | Execute unit tests           |
| make start-db  | Start PostgreSQL container   |
| make migrate   | Apply database migrations    |
| make build-api | Build Docker image           |
| make run-api   | Start complete application   |

---

# Security

* Do not commit `.env` files to GitHub.
* Never store database passwords in source code.
* Use environment variables for sensitive information.
* Use `.dockerignore` and `.gitignore` to exclude unnecessary files.

---

# Future Enhancements

* CI Pipeline using GitHub Actions
* Bare Metal Deployment
* Kubernetes Deployment
* Helm Charts
* ArgoCD Continuous Deployment
* Observability Stack
* Dashboards and Alerts

---

# Author

**Aditya**

Student CRUD REST API Project built for learning:

* Backend Development
* DevOps
* Docker
* Docker Compose
* PostgreSQL
* SQLAlchemy ORM
* CI/CD
* Kubernetes
* Cloud Engineering