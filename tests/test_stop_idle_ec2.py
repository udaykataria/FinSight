import pytest
import boto3
from moto import mock_ec2
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'lambdas'))

from stop_idle_ec2 import lambda_handler


@mock_ec2
def test_lambda_handler_no_instances():
    """Test lambda handler when no EC2 instances are running"""
    result = lambda_handler({}, {})
    assert result["StoppedInstances"] == []


@mock_ec2
def test_lambda_handler_with_running_instances():
    """Test lambda handler with running EC2 instances"""
    # Create mock EC2 instances
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instances = ec2.create_instances(ImageId='ami-12345678', MinCount=2, MaxCount=2)
    
    # Test the lambda handler
    result = lambda_handler({}, {})
    
    # Should return 2 stopped instance IDs
    assert len(result["StoppedInstances"]) == 2
    
    # Verify instances are actually stopped
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    for instance_id in result["StoppedInstances"]:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        assert state in ['stopping', 'stopped']


@mock_ec2
def test_lambda_handler_with_mixed_instance_states():
    """Test lambda handler with both running and stopped instances"""
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    # Create instances
    instances = ec2.create_instances(ImageId='ami-12345678', MinCount=3, MaxCount=3)
    
    # Stop one instance manually
    instances[0].stop()
    
    # Test the lambda handler (should only affect running instances)
    result = lambda_handler({}, {})
    
    # Should return 2 stopped instance IDs (the ones that were running)
    assert len(result["StoppedInstances"]) == 2