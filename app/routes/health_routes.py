from flask import Blueprint

health_bp = Blueprint(
    "health_bp",
    __name__
)


@health_bp.route(
    "/healthcheck",
    methods=["GET"]
)
def healthcheck():

    return {
        "status": "UP"
    }, 200
