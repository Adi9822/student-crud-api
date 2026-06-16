from app import create_app


def test_healthcheck():

    app = create_app()

    client = app.test_client()

    response = client.get("/healthcheck")

    assert response.status_code == 200


def test_get_students():

    app = create_app()

    client = app.test_client()

    response = client.get("/api/v1/students")

    assert response.status_code == 200