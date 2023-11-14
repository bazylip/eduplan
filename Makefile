VENV_DIR = venv
REQUIREMENTS_FILE = requirements.txt

activate-venv:
	@echo "Activating virtual environment..."
	@. $(VENV_DIR)/bin/activate && pip --version

pip-compile: activate-venv
	@echo "Compiling requirements..."
	@pip-compile -v --no-emit-index-url --output-file=$(REQUIREMENTS_FILE) requirements.in

build: activate-venv pip-compile
	@echo "Installing requirements into virtual environment..."
	@${VENV_DIR}/bin/python -m pip install -r requirements.txt
