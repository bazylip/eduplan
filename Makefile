VENV_DIR = venv
REQUIREMENTS_FILE = requirements.txt

activate-venv:
	@echo "Activating virtual environment..."
	@. $(VENV_DIR)/bin/activate && pip --version

pip-compile:
	docker-compose run app bash -c \
	"pip-compile -v --no-emit-index-url \
	--output-file=requirements.txt requirements.in"

dev-pip-compile:
	docker-compose run app bash -c \
	"pip-compile -v --no-emit-index-url \
	--output-file=requirements-dev.txt requirements.in requirements-dev.in"

build:
	docker-compose build

up:
	docker-compose up app

test:
	docker-compose up --build test

run:
	docker-compose run app sh
