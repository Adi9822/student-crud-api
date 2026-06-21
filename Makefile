install:
	pip install -r requirements.txt

run:
	python run.py

test:
	pytest

migrate:
	flask --app run.py db upgrade

build-api:
	docker build -t student-api:1.0.0 .

run-api: 
	start-db migrate build-api
	docker compose up -d

docker-build:
	docker build -t student-api:1.0.0 .

docker-run:
	docker run -p 5000:5000 -e DB_HOST=host.docker.internal -e DB_PORT=5432 -e DB_NAME=studentdb -e DB_USER=<your-db-user> -e DB_PASSWORD=<your-db-password> student-api:1.0.0