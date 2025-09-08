.PHONY: help install install-dev test lint format clean build docker-build docker-run terraform-init terraform-plan terraform-apply

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black"
	@echo "  clean        - Clean up build artifacts"
	@echo "  build        - Build Python package"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"
	@echo "  terraform-init    - Initialize Terraform"
	@echo "  terraform-plan    - Plan Terraform changes"
	@echo "  terraform-apply   - Apply Terraform changes"

# Python package management
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -e .[dev]

# Testing and quality
test:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

test-fast:
	pytest tests/ -v

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

# Build and packaging
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean
	python setup.py sdist bdist_wheel

# Docker commands
docker-build:
	docker build -t finsight-cloud-monitoring .

docker-run:
	docker-compose up finsight-cost-monitor

docker-dev:
	docker-compose up finsight-dev

docker-test:
	docker-compose up finsight-test

# Terraform commands
terraform-init:
	cd src/terraform && terraform init

terraform-plan:
	cd src/terraform && terraform plan

terraform-apply:
	cd src/terraform && terraform apply

terraform-destroy:
	cd src/terraform && terraform destroy

# Development workflow
setup: install-dev
	pre-commit install

check: lint test

ci: check build

# AWS commands
aws-costs:
	python src/scripts/fetch_daily_costs.py

deploy-lambda:
	cd src/lambdas && zip -r stop_idle_ec2.zip stop_idle_ec2.py
	@echo "Upload stop_idle_ec2.zip to AWS Lambda"