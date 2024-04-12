.PHONY: install
install:
	poetry install --no-root

#.PHONY: install-pre-commit
#install-pre-commit:
#	poetry run pre-commit uninstall; poetry run pre-commit install --hook-type commit-msg

.PHONY: lint
lint:
	poetry run pre-commit run


.PHONY: run-server
run-server:
	poetry run python core/manage.py runserver

.PHONY: migrations
migrations:
	poetry run python core/manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python core/manage.py migrate

.PHONY: shell
shell:
	poetry run python core/manage.py shell

.PHONY: test
test:
	poetry run pytest core


.PHONY: flake8
flake8:
	poetry run  flake8