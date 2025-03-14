PORT=8080
HOST=0.0.0.0

setup:
	uv sync
	uv run src/manage.py makemigrations

setup-dev: setup
	uv run pre-commit install

migration:
	uv run src/manage.py makemigrations
	uv run src/manage.py migrate

run:
	uv run src/manage.py runserver $(HOST):$(PORT)

run-dev:
	DEBUG=True ALLOWED_HOSTS=* uv run src/manage.py runserver $(HOST):$(PORT)

unit-test:
	uv run src/manage.py test --tag=unit

feature-test:
	uv run src/manage.py test --tag=feature

e2e-test:
	uv run src/manage.py test --tag=e2e

test:
	uv run src/manage.py test

export-swagger:
	uv run src/manage.py spectacular --file swagger/api.yaml
