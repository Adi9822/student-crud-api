# Student CRUD REST API

## Overview

This project is a Student CRUD REST API built using:

* Python
* Flask
* PostgreSQL
* SQLAlchemy
* Flask-Migrate

The API supports creating, reading, updating, and deleting student records.

---

## Features

* Create Student
* Get All Students
* Get Student By ID
* Update Student
* Delete Student
* Health Check Endpoint
* PostgreSQL Database
* Database Migrations
* Environment Variable Configuration
* Logging
* Unit Tests

---

## Project Structure

student-api/

├── app/

├── migrations/

├── tests/

├── run.py

├── requirements.txt

├── README.md

└── .env

---

## Setup

### Clone Repository

git clone <repository-url>

cd student-api

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Database Migrations

flask --app run.py db upgrade

### Start Application

python run.py

---

## Health Check

GET /healthcheck

---

## API Endpoints

POST /api/v1/students

GET /api/v1/students

GET /api/v1/students/<id>

PUT /api/v1/students/<id>

DELETE /api/v1/students/<id>

---

## Run Tests

pytest