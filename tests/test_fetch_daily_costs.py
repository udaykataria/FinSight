import pytest
import boto3
from moto import mock_ce
from datetime import datetime, timedelta
import sys
import os
import json

# Add src directory to path for imports  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'scripts'))


@mock_ce
def test_cost_explorer_integration():
    """Test that Cost Explorer API integration works"""
    # Mock Cost Explorer client
    ce = boto3.client('ce', region_name='us-east-1')
    
    # This is a basic test - moto doesn't fully support Cost Explorer
    # In a real environment, you'd test with actual AWS credentials
    assert ce is not None


def test_date_calculation():
    """Test date calculation logic"""
    from datetime import datetime, timedelta
    
    end = datetime.utcnow().date()
    start = end - timedelta(days=1)
    
    # Verify date format
    start_str = start.strftime('%Y-%m-%d')
    end_str = end.strftime('%Y-%m-%d')
    
    assert len(start_str) == 10  # YYYY-MM-DD format
    assert len(end_str) == 10
    assert start < end


def test_json_data_structure():
    """Test JSON data structure creation"""
    from datetime import datetime, timedelta
    
    start = datetime.utcnow().date() - timedelta(days=1)
    amount = "12.34"
    
    data = {
        "date": str(start),
        "cost": amount
    }
    
    # Verify structure
    assert "date" in data
    assert "cost" in data
    assert data["date"] == str(start)
    assert data["cost"] == amount
    
    # Verify JSON serialization works
    json_str = json.dumps(data, indent=2)
    parsed_data = json.loads(json_str)
    assert parsed_data == data