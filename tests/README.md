# Tests

This directory contains comprehensive tests for the FinSight Cloud Monitoring & Optimization project.

## Test Structure

```
tests/
├── test_stop_idle_ec2.py      # Tests for Lambda function
├── test_fetch_daily_costs.py  # Tests for cost fetching script
└── conftest.py                # Pytest configuration and fixtures
```

## Running Tests

### Prerequisites
```bash
pip install pytest moto boto3
```

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_stop_idle_ec2.py -v
```

### Run with Coverage
```bash
pytest tests/ --cov=src --cov-report=html
```

## Test Categories

### Unit Tests
- Lambda function logic
- Cost calculation functions
- Data structure validation

### Integration Tests
- AWS service mocking with moto
- End-to-end workflow testing

### Mock Services
We use `moto` library to mock AWS services:
- EC2 for instance management testing
- Cost Explorer for cost tracking testing

## CI/CD Integration

Tests are automatically run in GitHub Actions on:
- Pull requests
- Pushes to main branch
- Scheduled nightly runs

## Writing New Tests

When adding new functionality:
1. Write tests first (TDD approach)
2. Use appropriate mocking for AWS services
3. Follow existing test patterns
4. Include both positive and negative test cases
5. Add integration tests for complex workflows

## Test Data

Mock data and fixtures are defined in `conftest.py` for consistency across tests.