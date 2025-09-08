# 💸 FinSight — Cloud Monitoring & Cost Optimization (AWS)

[![CI/CD Pipeline](https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization/actions/workflows/ci.yml/badge.svg)](https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📌 Overview
FinSight is a **cloud cost monitoring and optimization project** built on AWS. It tracks daily usage, detects cost spikes, automates idle resource shutdown, and provides a **single CloudWatch dashboard** for cost + performance visibility.

✅ Inspired by real-world Cloud Engineer responsibilities  
✅ Implemented with **automation, monitoring, and security-first design**  
✅ Deployed fully on **AWS Free Tier**  
✅ **Professional repository structure** with CI/CD, testing, and documentation

---

## 🏗️ Architecture

### Components
- **AWS CloudWatch** → Monitors metrics (EC2 CPU, Network, EBS IOPS, Billing)
- **AWS Lambda** → Automates daily cost checks & stops idle EC2
- **AWS EventBridge** → Triggers Lambda on schedule (daily/hourly)
- **AWS Cost Explorer API** → Fetches actual cost data
- **S3 (Optional)** → Store cost logs/reports
- **IAM Roles** → Least-privilege security policies for Lambda & EC2

### Data Flow
```
CloudWatch Alarm (CPUUtilization < 5%)  
➡ SNS Topic  
➡ Lambda (StopIdleEC2)  
➡ Stops EC2 Instances  
➡ Sends Notification (SNS Destination)
```

---

## 📂 Project Structure

```
FinSight-Cloud-monitoring-and-optimization/
├── 📁 src/                         # Source code
│   ├── 📁 lambdas/                 # AWS Lambda functions
│   │   └── stop_idle_ec2.py
│   ├── 📁 scripts/                 # Utility scripts
│   │   └── fetch_daily_costs.py
│   └── 📁 terraform/               # Infrastructure as Code
│       └── provider.tf
├── 📁 tests/                       # Comprehensive tests
│   ├── test_stop_idle_ec2.py
│   ├── test_fetch_daily_costs.py
│   └── conftest.py
├── 📁 docs/                        # Documentation
│   ├── dashboard-setup.md
│   └── dashboard-config.json
├── 📁 daily-progress/              # Implementation journal
│   ├── day1-architecture/
│   ├── day2/ ... day10/
│   └── DAY1_NOTES.md
├── 📁 .github/                     # GitHub templates & workflows
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── 📄 README.md                    # This file
├── 📄 CONTRIBUTING.md              # Contribution guidelines
├── 📄 LICENSE                      # MIT License
├── 📄 requirements.txt             # Python dependencies
├── 📄 setup.py                     # Package configuration
├── 📄 Dockerfile                   # Container configuration
├── 📄 docker-compose.yml           # Multi-container setup
├── 📄 Makefile                     # Development commands
└── 📄 .pre-commit-config.yaml      # Code quality hooks
```

---

## 🔑 Key Features
1. **Daily Cost Tracking** (Lambda + Cost Explorer API)
2. **Billing Alerts** (SNS notifications when thresholds breached)
3. **Idle Resource Automation** (EC2 auto-stop when idle)
4. **CloudWatch Dashboard** (cost trends + usage metrics)
5. **Testing Simulations** (high usage, cost spikes, idle states)
6. **Security** (IAM least-privilege roles)
7. **CI/CD Pipeline** (Automated testing and deployment)
8. **Professional Code Quality** (Linting, formatting, pre-commit hooks)

---

## 🚀 Quick Start

### Prerequisites
- AWS Account (Free Tier)
- Python 3.8+
- AWS CLI configured
- Docker (optional)

### Installation

#### Option 1: Local Development
```bash
# Clone repository
git clone https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization.git
cd FinSight-Cloud-monitoring-and-optimization

# Install dependencies
pip install -r requirements.txt

# Run cost monitoring
python src/scripts/fetch_daily_costs.py
```

#### Option 2: Docker
```bash
# Build and run with Docker
docker-compose up finsight-cost-monitor

# For development
docker-compose up finsight-dev
```

#### Option 3: Development Setup
```bash
# Complete development setup
make setup
make test
make lint
```

### Key Files & Usage
- **Lambda Function**: `src/lambdas/stop_idle_ec2.py` → Deploy to AWS Lambda
- **Cost Script**: `src/scripts/fetch_daily_costs.py` → Run locally or in Lambda
- **Dashboard**: `docs/dashboard-config.json` → Import to CloudWatch
- **Infrastructure**: `src/terraform/` → Deploy with Terraform

---

## 🧪 Testing & Quality Assurance

### Running Tests
```bash
# Run all tests
make test

# Quick test run
make test-fast

# Run specific test
pytest tests/test_stop_idle_ec2.py -v
```

### Code Quality
```bash
# Check code quality
make lint

# Format code
make format

# Run all quality checks
make check
```

### CI/CD Pipeline
- ✅ **Automated Testing** on every PR
- ✅ **Code Quality Checks** (linting, formatting)
- ✅ **Security Scanning** with Trivy
- ✅ **Terraform Validation**

---

## 🧪 Validation Results

### High Usage Simulation
- ✅ Ran `stress` tool on EC2 to push CPU > 70%
- ✅ CloudWatch High-Usage Alarm successfully triggered

### Idle State Simulation  
- ✅ Left EC2 idle, CPU < 5% for 15 mins
- ✅ CloudWatch Alarm triggered Lambda → EC2 stopped automatically
- ✅ Verified in EC2 console + Lambda logs

### Testing Coverage
- ✅ **Unit Tests**: Lambda functions and scripts
- ✅ **Integration Tests**: AWS service mocking
- ✅ **End-to-End Tests**: Complete workflow validation

---

## 📈 STAR Method Summary

- **Situation** – Cloud costs can rise unnoticed in dynamic environments
- **Task** – Needed to design a monitoring + automation system to control AWS costs
- **Action** – Built an AWS-native solution using **CloudWatch, Lambda, Cost Explorer API, EventBridge, and IAM least-privilege roles** with professional development practices including CI/CD, testing, and documentation
- **Result** – Delivered a **production-ready, cost-optimized, automated monitoring system** with daily reporting, dashboards, comprehensive testing, and maintainable code structure that reduces cloud wastage risk and improves visibility

---

## 🛠️ Technologies Used

### AWS Services
- **Compute**: EC2, Lambda
- **Monitoring**: CloudWatch, SNS
- **Cost Management**: Cost Explorer API
- **Security**: IAM
- **Storage**: S3 (optional)
- **Automation**: EventBridge

### Development Stack
- **Language**: Python 3.8+
- **Testing**: pytest, moto (AWS mocking)
- **Code Quality**: black, flake8, mypy, pre-commit
- **CI/CD**: GitHub Actions
- **Infrastructure**: Terraform
- **Containerization**: Docker, Docker Compose
- **Documentation**: Markdown, GitHub Pages ready

### Region
- **Primary**: ap-northeast-1 (Asia Pacific - Tokyo)

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- Development setup
- Code standards
- Testing requirements
- Pull request process

### Quick Contribution Setup
```bash
# Set up development environment
make setup

# Make your changes, then
make check  # Run all quality checks
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- 📚 [Documentation](docs/)
- 🐛 [Report Bug](https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization/issues)
- 💡 [Request Feature](https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization/issues)
- 📈 [Project Roadmap](daily-progress/)

---

This project demonstrates **production-ready cloud engineering skills** including cost optimization, automation, monitoring, security best practices, professional code organization, testing, and CI/CD — all essential capabilities for modern cloud infrastructure management.
