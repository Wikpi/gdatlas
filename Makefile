.PHONY: build install test help clean-cache lint format format-check venv

PACKAGE := gdatlas

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PROJECT_DIR ?= .

run:
	@echo "Running package..."
	@$(PYTHON) -m $(PACKAGE) $(PROJECT_DIR) $(ARGS)

build:
	@echo "Building package..."
	@$(PYTHON) -m build $(PROJECT_DIR)

install:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python -m venv $(VENV); \
	fi

	@echo "Installing package in editable mode..."
	@$(PIP) install -e ".[dev]"

test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest -v $(PROJECT_DIR)

lint:
	@echo "Running linter..."
	@$(PYTHON) -m ruff check $(PROJECT_DIR)

format-check:
	@echo "Checking code formatting..."
	@$(PYTHON) -m ruff format --check $(PROJECT_DIR)

format:
	@echo "Formatting code..."
	@$(PYTHON) -m ruff format $(PROJECT_DIR)

clean-cache:
	@echo "Cleaning package cache..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

help:
	@echo "No current help available."