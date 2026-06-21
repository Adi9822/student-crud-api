from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        "app.config.config.Config"
    )

    db.init_app(app)

    from app.models.student import Student  # noqa: F401
    from app.routes.student_routes import student_bp
    from app.routes.health_routes import health_bp

    app.register_blueprint(student_bp)
    app.register_blueprint(health_bp)

    return app
