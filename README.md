# 💸 FinSight — Cloud Monitoring & Cost Optimization (AWS)

## 📌 Overview
FinSight is a **cloud cost monitoring and optimization project** built on AWS. It tracks daily usage, detects cost spikes, automates idle resource shutdown, and provides a **single CloudWatch dashboard** for cost + performance visibility.

✅ Inspired by real-world Cloud Engineer responsibilities  
✅ Implemented with **automation, monitoring, and security-first design**  
✅ Deployed fully on **AWS Free Tier**

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

## 🔑 Key Features
1. **Daily Cost Tracking** (Lambda + Cost Explorer API)
2. **Billing Alerts** (SNS notifications when thresholds breached)
3. **Idle Resource Automation** (EC2 auto-stop when idle)
4. **CloudWatch Dashboard** (cost trends + usage metrics)
5. **Testing Simulations** (high usage, cost spikes, idle states)
6. **Security** (IAM least-privilege roles)

---

## ⚙️ How It Works
1. CloudWatch/EventBridge triggers **daily Lambda** → fetches billing cost via Cost Explorer → logs cost → optional save to S3
2. If cost > threshold → **SNS notification** → email alert
3. CloudWatch metrics track **EC2 performance & cost trends**
4. Lambda automation checks idle EC2 → stops instances to save cost
5. Dashboard aggregates **cost + usage metrics** for visibility

---

## 📂 Project Structure & Daily Progress
- **Day 1:** Initial setup & environment
- **Day 2:** EC2 Instance Setup & SSH Connection
- **Day 3:** Custom CloudWatch metrics
- **Day 4:** Lambda for cost tracker
- **Day 5:** Daily cost monitoring automation
- **Day 6:** Stop idle EC2 automation
- **Day 7:** Testing (high usage/cost/idle simulations)
- **Day 8:** CloudWatch dashboard
- **Day 9:** Security & IAM least-privilege
- **Day 10:** Final documentation & GitHub

---

## 🚀 Quick Start

### Prerequisites
- AWS Account (Free Tier)
- AWS CLI configured
- Terraform (optional)

### Repository Setup
```bash
git clone https://github.com/udaykataria/FinSight-Cloud-monitoring-and-optimization.git
cd FinSight-Cloud-monitoring-and-optimization
```

### Key Files
- `day6-automation/stop_idle_ec2.py` → Lambda function to stop idle EC2
- `python/fetch_daily_costs.py` → Daily cost fetching script
- `dashboard-config.json` → CloudWatch dashboard configuration
- `day9/iam-policies.md` → Security policies and IAM setup
- Various day-specific README files for detailed implementation steps

---

## 🧪 Testing & Validation

### High Usage Simulation
- Ran `stress` tool on EC2 to push CPU > 70%
- CloudWatch High-Usage Alarm successfully triggered

### Idle State Simulation  
- Left EC2 idle, CPU < 5% for 15 mins
- CloudWatch Alarm triggered Lambda → EC2 stopped automatically
- Verified in EC2 console + Lambda logs

### Cost Spike Simulation
- Uploaded fake high-cost JSON to S3 (`$150` for EC2)
- Verified GitHub `/daily-costs/` updated with new cost entry

✅ **Proven Results:**
- Monitoring works ✅
- Automation works ✅  
- Cost tracking works ✅

---


**STAR Method Summary:**
- **Situation** – Cloud costs can rise unnoticed in dynamic environments
- **Task** – Needed to design a monitoring + automation system to control AWS costs
- **Action** – Built an AWS-native solution using **CloudWatch, Lambda, Cost Explorer API, EventBridge, and IAM least-privilege roles** to track usage, send alerts, and stop idle EC2 automatically
- **Result** – Delivered a **cost-optimized, automated monitoring system** with daily reporting and dashboards, reducing cloud wastage risk and improving visibility

---

## 🛠️ Technologies Used
- **AWS Services:** EC2, CloudWatch, Lambda, EventBridge, SNS, Cost Explorer API, S3, IAM
- **Languages:** Python
- **Infrastructure:** Terraform (optional)
- **Region:** ap-northeast-1 (Asia Pacific - Tokyo)

---

This project demonstrates practical cloud engineering skills including cost optimization, automation, monitoring, and security best practices — all essential capabilities for modern cloud infrastructure management.
