import pytest
import os
import tempfile


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files"""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def mock_aws_credentials():
    """Mock AWS credentials for testing"""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
    yield
    # Clean up
    for key in ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", 
                "AWS_SECURITY_TOKEN", "AWS_SESSION_TOKEN", "AWS_DEFAULT_REGION"]:
        if key in os.environ:
            del os.environ[key]


@pytest.fixture
def sample_cost_data():
    """Sample cost data for testing"""
    return {
        "ResultsByTime": [
            {
                "Total": {
                    "UnblendedCost": {
                        "Amount": "12.34",
                        "Unit": "USD"
                    }
                },
                "TimePeriod": {
                    "Start": "2024-01-01",
                    "End": "2024-01-02"
                }
            }
        ]
    }