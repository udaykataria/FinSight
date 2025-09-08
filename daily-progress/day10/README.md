# 💸 FinSight – Cloud Monitoring & Cost Optimization (AWS)

## 📌 Overview
FinSight is a **cloud cost monitoring and optimization project** built on AWS.  
It tracks daily usage, detects cost spikes, automates idle resource shutdown, and provides a **single CloudWatch dashboard** for cost + performance visibility.  

✅ Inspired by real-world Cloud Engineer responsibilities.  
✅ Implemented with **automation, monitoring, and security-first design**.  
✅ Deployed fully on **AWS Free Tier**.  

---

## 🏗️ Architecture

![Architecture](./architecture-diagram.png)

### Components
- **AWS CloudWatch** → Monitors metrics (EC2 CPU, Network, EBS IOPS, Billing).
- **AWS Lambda** → Automates daily cost checks & stops idle EC2.
- **AWS EventBridge** → Triggers Lambda on schedule (daily/hourly).
- **AWS Cost Explorer API** → Fetches actual cost data.
- **S3 (Optional)** → Store cost logs/reports.
- **IAM Roles** → Least-privilege security policies for Lambda & EC2.

---

## 🔑 Features
1. **Daily Cost Tracking** (Lambda + Cost Explorer API).
2. **Billing Alerts** (SNS notifications when thresholds breached).
3. **Idle Resource Automation** (EC2 auto-stop when idle).
4. **CloudWatch Dashboard** (cost trends + usage metrics).
5. **Testing Simulations** (high usage, cost spikes, idle states).
6. **Security** (IAM least-privilege roles).

---

## ⚙️ How It Works
1. CloudWatch/EventBridge triggers **daily Lambda** → fetches billing cost via Cost Explorer → logs cost → optional save to S3.  
2. If cost > threshold → **SNS notification** → email alert.  
3. CloudWatch metrics track **EC2 performance & cost trends**.  
4. Lambda automation checks idle EC2 → stops instances to save cost.  
5. Dashboard aggregates **cost + usage metrics** for visibility.  

---

## 📂 Project Days
- **Day 1:** Initial setup & environment
- **Day 2:** Billing alerts (SNS + Budgets)
- **Day 3:** Custom CloudWatch metrics
- **Day 4:** Lambda for cost tracker
- **Day 5:** Daily cost monitoring automation
- **Day 6:** Stop idle EC2 automation
- **Day 7:** Testing (high usage/cost/idle)
- **Day 8:** CloudWatch dashboard
- **Day 9:** Security & IAM least-privilege
- **Day 10:** Final documentation & GitHub

---

## 📸 Screenshots
- CloudWatch dashboard
- Lambda logs
- Billing alerts
- IAM policies
- Architecture diagram

---

## 📜 Resume STAR Bullet
**Situation** – Cloud costs can rise unnoticed in dynamic environments.  
**Task** – Needed to design a monitoring + automation system to control AWS costs.  
**Action** – Built an AWS-native solution using **CloudWatch, Lambda, Cost Explorer API, EventBridge, and IAM least-privilege roles** to track usage, send alerts, and stop idle EC2 automatically.  
**Result** – Delivered a **cost-optimized, automated monitoring system** with daily reporting and dashboards, reducing cloud wastage risk and improving visibility.  

**Resume Bullet:**  
*Developed and deployed a cost monitoring & optimization system on AWS (CloudWatch, Lambda, EventBridge, Cost Explorer API) that automated daily cost tracking, sent real-time billing alerts, and stopped idle EC2 instances — improving cost visibility and reducing unnecessary expenses.*  

---

## 🚀 How to Reproduce
1. Clone repo:  
   ```bash
   git clone https://github.com/<your-username>/FinSight-Cloud-Monitoring-Optimization.git
