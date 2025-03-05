PORT=8080
HOST=0.0.0.0
COVERAGE_TARGET=src

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
	uv run pytest -m unit

feature-test:
	uv run pytest -m feature

e2e-test:
	uv run pytest -m e2e

test:
	uv run pytest

ptw:
	uv run ptw .

test-report:
	uv run pytest --cov-report term-missing --cov=$(COVERAGE_TARGET)
	uv run coverage html

export-swagger:
	uv run src/manage.py spectacular --file swagger/api.yaml
