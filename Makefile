SHOW_INFO_ICON = $(shell printf "\033[34;1m▶\033[0m")
SHOW_SUCCESS_ICON = $(shell printf "\033[32;1m✔\033[0m")

run_dev: setup_env
	$(info $(SHOW_INFO_ICON) Running in development mode ...)
	docker-compose up --build

run_prod: setup_env
	$(info $(SHOW_INFO_ICON) Running app ...)
	docker-compose up

.PHONY: lint
lint:
	flake8 sennder/movies

.PHONY: type
type:
	mypy sennder/movies

.PHONY: test
test:
	coverage run --source='./sennder/movies' ./manage.py test
	coverage report

.PHONY: setup_env
setup_env: # helpful for this task to avoid creating a manual env file
	touch .env
	cp .env.example .env

setup_venv: setup_env
	$(info $(SHOW_INFO_ICON) Setting up environment ...)
	python3 -m venv .venv
	. .venv/bin/activate
	pip3 install -r requirements.txt
	$(info $(SHOW_SUCCESS_ICON) Env setup complete)