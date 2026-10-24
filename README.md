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

# Kubernetes Deployment (Milestones 6–7)

## Architecture

The Student CRUD REST API runs in Kubernetes with:
- Flask REST API exposed through a Kubernetes Service.
- PostgreSQL deployed as a StatefulSet with persistent storage.
- ConfigMap for database configuration.
- HashiCorp Vault and External Secrets Operator (ESO) for database credentials.
- Database migrations executed by an init container before the API starts.
- Health checks using `/healthcheck`.

## Prerequisites

Install Docker, kubectl, Minikube, and Helm.

## Kubernetes Node Placement

The cluster uses these node labels:

- `type=application` — Student API
- `type=database` — PostgreSQL
- `type=dependent_services` — Vault and dependent services

Check node labels:

```powershell
kubectl get nodes --show-labels
```

## Deploy PostgreSQL and Secrets

Install External Secrets Operator and HashiCorp Vault before deploying the application. Configure Vault with the database username and password, create a read-only Vault policy, and configure the ESO token Secret. Never commit credentials or tokens to GitHub.

Apply the secret store and database manifests:

```powershell
kubectl apply -f .\k8s\external-secrets.yml
kubectl apply -f .\k8s\database.yml
kubectl get externalsecret -n student-api
kubectl get pods,pvc -n student-api
```

Wait until the database is running and its external Secret is synchronized.

## Deploy the Student API

Build and load the Docker image into Minikube:

```powershell
docker build -t student-api:1.0.0 .
minikube image load student-api:1.0.0 -p sre-bootcamp
```

Apply the API manifest:

```powershell
kubectl apply -f .\k8s\application.yml
kubectl rollout status deployment/student-api -n student-api --timeout=180s
kubectl get pods,services -n student-api
```

The API's init container runs database migrations before the application starts.

## Access and Test the API

Start port forwarding in a separate PowerShell window:

```powershell
kubectl port-forward -n student-api service/student-api 5000:5000
```

In another PowerShell window, test the health endpoint:

```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/healthcheck'
```

Expected response:

```json
{"status":"UP"}
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/healthcheck` | Health check |
| POST | `/api/v1/students` | Create a student |
| GET | `/api/v1/students` | List students |
| GET | `/api/v1/students/<id>` | Get a student |
| PUT | `/api/v1/students/<id>` | Update a student |
| DELETE | `/api/v1/students/<id>` | Delete a student |

Use the Postman collection at `postman/Student CRUD API.postman_collection.json` to test the endpoints.

## Troubleshooting

```powershell
kubectl get pods -A
kubectl get events -n student-api
kubectl logs deployment/student-api -n student-api
kubectl describe externalsecret student-api-db-credentials -n student-api
```

Do not commit passwords, Vault tokens, or `.env` files to GitHub.

**Note:** The Vault development configuration is for learning only. Its in-memory data may be lost when Vault restarts.

# Helm Deployment (Milestone 8)

## Helm Chart Structure

The project contains two Helm charts:

- `helm/postgres` — PostgreSQL StatefulSet, headless Service, ConfigMap, and persistent storage.
- `helm/student-api` — Flask REST API Deployment, Service, configuration, and database migration init container.

Both charts use the existing `student-api-db-secret` created by External Secrets Operator (ESO). Vault, ESO, and the ExternalSecret must be configured before deploying the application.

## Validate the Charts

Run these commands from the project root:

```powershell
helm lint .\helm\postgres
helm lint .\helm\student-api

helm template postgres .\helm\postgres --namespace student-api
helm template student-api .\helm\student-api --namespace student-api
```

## Install or Upgrade the Releases

```powershell
helm upgrade --install postgres .\helm\postgres --namespace student-api --create-namespace --wait --timeout 5m

helm upgrade --install student-api .\helm\student-api --namespace student-api --wait --timeout 5m
```

If Kubernetes resources already exist from standalone manifests, review the rendered charts and resource differences before adopting them into Helm.

## Verify Deployment and Test

```powershell
helm list -n student-api
helm status postgres -n student-api
helm status student-api -n student-api

kubectl get deployment,statefulset,pods,services,pvc -n student-api
kubectl rollout status deployment/student-api -n student-api --timeout=180s

helm test student-api -n student-api
```

## Access the Health Endpoint

Start port forwarding in one terminal:

```powershell
kubectl port-forward service/student-api 5000:5000 -n student-api
```

In another terminal:

```powershell
Invoke-RestMethod http://localhost:5000/healthcheck
```

The expected health status is `UP`. Stop port forwarding with `Ctrl+C` when finished.

## Persistent Storage Safety

PostgreSQL uses persistent storage. Verify that `data-postgres-0` remains `Bound` after deployment and upgrades. Do not delete the PVC or force-replace the StatefulSet as a routine troubleshooting step, because this can risk database availability or data loss.