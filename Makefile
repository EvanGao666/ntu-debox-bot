# Variables
PYTHON := python
PIP := pip
PYTEST := pytest

# Default target
all: test

# Install dependencies
install:
	$(PIP) install -r requirements.txt
	$(PIP) install pytest

# Run tests
test:
	$(PYTEST) tests/

# Clean up
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache

# Help
help:
	@echo "Makefile commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make test      - Run all tests"
	@echo "  make clean     - Clean up generated files"

