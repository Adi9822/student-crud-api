install:
	pip install -r requirements.txt

run:
	python run.py

test:
	pytest

migrate:
	flask --app run.py db upgrade