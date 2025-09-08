#!/usr/bin/env python3
"""
FinSight Cloud Monitoring & Optimization
Setup script for Python package installation
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="finsight-cloud-monitoring",
    version="1.0.0",
    author="FinSight Team",
    author_email="your-email@example.com",
    description="AWS Cloud Monitoring & Cost Optimization Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization",
    project_urls={
        "Bug Tracker": "https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization/issues",
        "Documentation": "https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization/blob/main/docs/",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "moto[ec2,cloudwatch]>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "finsight-costs=scripts.fetch_daily_costs:main",
        ],
    },
)