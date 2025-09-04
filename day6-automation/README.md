# Day 6 — Automation: Stop Idle Resources

## 📌 Why Idle Detection Matters
Running idle EC2 instances wastes money.  
By using **CloudWatch Alarms + Lambda**, we automatically stop instances with very low CPU usage, reducing unnecessary AWS costs.

---

## ⚡ Architecture

CloudWatch Alarm (CPUUtilization < 5%)  
➡ SNS Topic  
➡ Lambda (StopIdleEC2)  
➡ Stops EC2 Instances  
➡ Sends Notification (SNS Destination)

---

## 📷 Screenshots to Add
1. CloudWatch Alarm configuration (`CPUUtilization < 5% for 15 minutes`).
2. Lambda logs showing instances stopped.
3. EC2 state change (Running ➝ Stopped).

---

## ✅ Files
- `stop_idle_ec2.py` → Lambda function to stop idle EC2.
- `README.md` → Documentation, architecture, and screenshots.
