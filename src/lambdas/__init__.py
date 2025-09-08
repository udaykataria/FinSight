"""AWS Lambda functions for cost optimization and monitoring."""

from .stop_idle_ec2 import lambda_handler

__all__ = ["lambda_handler"]