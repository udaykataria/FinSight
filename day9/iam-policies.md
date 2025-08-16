# 🔒 Day 9 – Security & IAM Policies

In this step, we configure **least-privilege IAM roles** for Lambda and EC2 to ensure secure access.

---

## ✅ Steps Taken

### 1. Lambda Execution Role
- Created IAM Role: `FinSight-Lambda-Execution-Role`
- Trusted entity: **Lambda**
- Attached policy: `lambda-policy.json` (custom least-privilege)
- Purpose: Allow Lambda only to:
  - Write to CloudWatch Logs
  - Describe EC2 instances
  - Stop/Start EC2 (for idle automation)
  - (Optional) Access S3 if cost files are used

---

### 2. EC2 Instance Role
- Created IAM Role: `FinSight-EC2-Monitoring-Role`
- Trusted entity: **EC2**
- Attached policy: `ec2-policy.json`
- Purpose: Allow EC2 instance only to:
  - Publish metrics/logs to CloudWatch
  - Read SSM Parameters (if needed for config)
  - No admin privileges

---

### 3. Best Practices Followed
- **Least-Privilege Access** (no * for actions).
- **Service-specific trust policies** (Lambda ↔ Lambda, EC2 ↔ EC2).
- **CloudWatch Logs enabled** for auditing.

---

## 📷 Screenshots
- `lambda-iam-role.png` – IAM Role for Lambda.
- `ec2-iam-role.png` – IAM Role for EC2.
