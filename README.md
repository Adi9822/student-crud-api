# Student CRUD REST API

## Overview

This project is a REST API for managing student records built using:

* Python
* Flask
* PostgreSQL
* SQLAlchemy ORM
* Flask-Migrate
* Docker

The API supports creating, reading, updating, and deleting student records and demonstrates backend development, database integration, testing, and containerization.

---

## Features

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
* Unit Testing with Pytest
* Docker Containerization
* Multi-stage Docker Build

---

## Tech Stack

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming Language |
| Flask         | REST API Framework   |
| PostgreSQL    | Database             |
| SQLAlchemy    | ORM                  |
| Flask-Migrate | Database Migrations  |
| Pytest        | Testing              |
| Docker        | Containerization     |

---

## Project Structure

student-api/

├── app/

│ ├── config/

│ ├── models/

│ ├── routes/

│ └── **init**.py

├── migrations/

├── tests/

├── Dockerfile

├── Makefile

├── .dockerignore

├── run.py

├── requirements.txt

├── README.md

└── .env

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd student-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

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

## Database Migration

Initialize migrations:

```bash
flask --app run.py db init
```

Create migration:

```bash
flask --app run.py db migrate -m "create students table"
```

Apply migration:

```bash
flask --app run.py db upgrade
```

---

## Run Application

```bash
python run.py
```

Application runs on:

```text
http://localhost:5000
```

---

## API Endpoints

### Health Check

```http
GET /healthcheck
```

Response:

```json
{
    "status": "UP"
}
```

---

### Create Student

```http
POST /api/v1/students
```

Request Body:

```json
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 22
}
```

Response:

```json
{
    "message": "Student created successfully",
    "id": 1
}
```

---

### Get All Students

```http
GET /api/v1/students
```

---

### Get Student By ID

```http
GET /api/v1/students/<id>
```

Example:

```http
GET /api/v1/students/1
```

---

### Update Student

```http
PUT /api/v1/students/<id>
```

Example Request:

```json
{
    "name": "Rahul Sharma",
    "age": 23
}
```

---

### Delete Student

```http
DELETE /api/v1/students/<id>
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Expected output:

```text
2 passed
```

---

## Docker

### Build Docker Image

```bash
docker build -t student-api:1.0.0 .
```

### View Docker Images

```bash
docker images
```

### Run Docker Container

```bash
docker run -p 5000:5000 \
-e DB_HOST=host.docker.internal \
-e DB_PORT=5432 \
-e DB_NAME=studentdb \
-e DB_USER=<your-db-user> \
-e DB_PASSWORD=<your-db-password> \
student-api:1.0.0
```

### Verify API Running

```bash
curl http://localhost:5000/healthcheck
```

Response:

```json
{
    "status": "UP"
}
```

---

## Makefile Commands

Install dependencies:

```bash
make install
```

Run application:

```bash
make run
```

Run tests:

```bash
make test
```

Build Docker image:

```bash
make docker-build
```

Run Docker container:

```bash
make docker-run
```

---

## Security

* Do not commit `.env` files to GitHub.
* Store database passwords securely.
* Inject environment variables at runtime.
* Keep secrets out of Docker images.

---

## Future Enhancements

* Docker Compose
* CI/CD Pipeline
* Kubernetes Deployment
* Helm Charts
* ArgoCD
* Monitoring and Alerting
* Observability Dashboard
