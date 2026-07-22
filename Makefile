.PHONY: build install test help clean-cache lint test venv

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

build:
	@echo "Building package..."
	@$(PYTHON) -m build

lint:
	@echo "No current lints available."

install:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python -m venv $(VENV); \
	fi

	@echo "Installing package in editable mode..."
	@$(PIP) install -e .

test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest

clean-cache:
	@echo "Cleaning package cache..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

help:
	@echo "No current help available."