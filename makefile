PORT=8080
HOST=0.0.0.0

setup:
	uv sync
	uv run manage.py makemigrations

migration:
	uv run manage.py migrate

run:
	uv run manage.py runserver $(HOST):$(PORT)

unit-test:
	uv run manage.py test --tag=unit

feature-test:
	uv run manage.py test --tag=feature

e2e-test:
	uv run manage.py test --tag=e2e

test:
	uv run manage.py test