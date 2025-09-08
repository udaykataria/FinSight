# Contributing to FinSight

Thank you for your interest in contributing to FinSight! This document provides guidelines for contributing to this project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/FinSight-Cloud-monitoring-and-optimization.git
   cd FinSight-Cloud-monitoring-and-optimization
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up AWS credentials** (for testing):
   ```bash
   aws configure
   ```

## Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards below

3. **Test your changes**:
   ```bash
   # Run Python tests
   pytest tests/
   
   # Run Terraform validation
   terraform validate
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: describe your changes"
   ```

5. **Push and create a Pull Request**

## Coding Standards

### Python
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions small and focused

### Terraform
- Use consistent naming conventions
- Add comments for complex configurations
- Follow Terraform best practices for security

### Documentation
- Update README.md if adding new features
- Include examples in your documentation
- Keep documentation clear and concise

## Project Structure

```
FinSight-Cloud-monitoring-and-optimization/
├── src/                    # Source code
│   ├── lambdas/           # Lambda functions
│   ├── scripts/           # Utility scripts
│   └── terraform/         # Infrastructure code
├── tests/                 # Test files
├── docs/                  # Documentation
├── .github/               # GitHub templates and workflows
└── daily-progress/        # Day-by-day implementation notes
```

## Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (AWS region, Python version, etc.)

## Questions?

Feel free to open an issue for questions or reach out to the maintainers.