.PHONY: build install test help clean-cache lint format format-check venv

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

build:
	@echo "Building package..."
	@$(PYTHON) -m build

install:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python -m venv $(VENV); \
	fi

	@echo "Installing package in editable mode..."
	@$(PIP) install -e ".[dev]"

test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest

lint:
	@echo "Running linter..."
	@$(PYTHON) -m ruff check .

format-check:
	@echo "Checking code formatting..."
	@$(PYTHON) -m ruff format --check .

format:
	@echo "Formatting code..."
	@$(PYTHON) -m ruff format .

clean-cache:
	@echo "Cleaning package cache..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

help:
	@echo "No current help available."