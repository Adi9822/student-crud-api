from flask import Blueprint
from flask import request

from app import db
from app.models.student import Student
import logging

student_bp = Blueprint(
    "student_bp",
    __name__
)


# CREATE STUDENT
@student_bp.route(
    "/api/v1/students",
    methods=["POST"]
)
def create_student():

    data = request.get_json()

    student = Student(
        name=data["name"],
        email=data["email"],
        age=data["age"]
    )

    db.session.add(student)
    logging.info(
    f"Creating student {student.email}"
)
    db.session.commit()

    return {
        "message": "Student created successfully",
        "id": student.id
    }, 201


# GET ALL STUDENTS
@student_bp.route(
    "/api/v1/students",
    methods=["GET"]
)
def get_students():

    students = Student.query.all()

    result = []

    for student in students:

        result.append({
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "age": student.age
        })

    return result, 200


# GET STUDENT BY ID
@student_bp.route(
    "/api/v1/students/<int:id>",
    methods=["GET"]
)
def get_student(id):

    student = Student.query.get(id)

    if not student:
        return {
            "message": "Student not found"
        }, 404

    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "age": student.age
    }, 200


# UPDATE STUDENT
@student_bp.route(
    "/api/v1/students/<int:id>",
    methods=["PUT"]
)
def update_student(id):

    student = Student.query.get(id)

    if not student:
        return {
            "message": "Student not found"
        }, 404

    data = request.get_json()

    student.name = data["name"]
    student.email = data["email"]
    student.age = data["age"]

    logging.info(
    f"Updating student {id}"
)

    db.session.commit()

    return {
        "message": "Student updated successfully"
    }, 200


# DELETE STUDENT
@student_bp.route(
    "/api/v1/students/<int:id>",
    methods=["DELETE"]
)
def delete_student(id):

    student = Student.query.get(id)

    if not student:
        return {
            "message": "Student not found"
        }, 404

    db.session.delete(student)

    logging.info(
    f"Deleting student {id}"
)
    db.session.commit()

    return {
        "message": "Student deleted successfully"
    }, 200