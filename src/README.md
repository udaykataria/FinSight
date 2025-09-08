# FinSight Source Code

This directory contains the core source code for the FinSight Cloud Monitoring & Optimization project.

## Structure

```
src/
├── lambdas/           # AWS Lambda functions
│   └── stop_idle_ec2.py
├── scripts/           # Utility scripts
│   └── fetch_daily_costs.py
└── terraform/         # Infrastructure as Code
    └── provider.tf
```

## Lambda Functions (`lambdas/`)

AWS Lambda functions for automation:
- `stop_idle_ec2.py` - Automatically stops idle EC2 instances to save costs

## Scripts (`scripts/`)

Utility scripts for monitoring and cost tracking:
- `fetch_daily_costs.py` - Fetches daily AWS costs using Cost Explorer API

## Terraform (`terraform/`)

Infrastructure as Code files:
- `provider.tf` - Terraform provider configurations

## Usage

### Lambda Functions
Deploy Lambda functions using the AWS CLI or Terraform.

### Scripts
Run scripts locally or in Lambda:
```bash
python src/scripts/fetch_daily_costs.py
```

### Terraform
```bash
cd src/terraform
terraform init
terraform plan
terraform apply
```