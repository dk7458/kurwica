


# Python version
PYTHON ?= python3

# Package name
PACKAGE := kurwica

# Installation directories
prefix ?= /usr/local
bindir := $(prefix)/bin
libdir := $(prefix)/lib/$(PACKAGE)

# Default target
.PHONY: all
all: install

# Install the package
.PHONY: install
install:
	$(PYTHON) setup.py install

# Run tests (to be implemented)
.PHONY: test
test:
	echo "Running tests..."
	# Add test commands here

# Clean build files
.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -f *.egg-info

# Show help
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo ""
	@echo "  make all        - Install the package"
	@echo "  make install    - Install the package"
	@echo "  make test       - Run tests (not implemented yet)"
	@echo "  make clean      - Clean build files"
	@echo "  make help       - Show this help message"

