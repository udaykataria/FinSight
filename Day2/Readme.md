# Day 2 - EC2 Instance Setup & SSH Connection

## Situation
The goal was to create a secure, cost-effective compute environment for the project platform.

## Task
Provision an AWS EC2 instance using the free tier and establish SSH connectivity.

## Actions
- Created a key pair and applied correct permissions (`chmod 400`).
- Launched a t2.micro instance (Amazon Linux 2023) under free tier.
- Configured security groups to allow SSH (port 22).
- Connected to the instance via SSH from the terminal.

## Results
- Successfully connected to the EC2 instance.
- Verified system readiness for application setup.
- Configured instance for future automation.

## Tools Used
- AWS EC2
- SSH
- Amazon Linux 2023
