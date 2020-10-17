run_dev: setup_env
	@echo "Running in development mode"
	docker-compose up

run_prod: setup_env
	@echo "Running in production mode"
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
	touch ./sennder/.env
	cp .env.example sennder/.env

setup_venv: setup_env
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt