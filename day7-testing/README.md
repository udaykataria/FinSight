# Day 7 — Testing & Simulation

## 🟢 High Usage Simulation
- Ran `stress` tool on EC2 to push CPU > 70%.
- CloudWatch High-Usage Alarm successfully triggered.

## 🔴 Idle State Simulation
- Left EC2 idle, CPU < 5% for 15 mins.
- CloudWatch Alarm triggered Lambda → EC2 stopped automatically.
- Verified in EC2 console + Lambda logs.

## 💰 Cost Spike Simulation
- Uploaded fake high-cost JSON to S3 (`$150` for EC2).
- Verified GitHub `/daily-costs/` updated with new cost entry.

---

## 📷 Screenshots to Add
1. CloudWatch Alarm in **ALARM** state (high usage).
2. Lambda logs showing EC2 stopped (idle).
3. GitHub repo `/daily-costs/` with test JSON.

---

✅ With this testing, we proved:
- Monitoring works ✅
- Automation works ✅
- Cost tracking works ✅
