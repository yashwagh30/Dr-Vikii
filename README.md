This repository demonstrates a **complete CI/CD pipeline** using **Docker, GitHub Actions, and Cloud Deployment**, with integrated **Monitoring (Prometheus + Grafana)** and **Security Scanning (Trivy)**.

---

🚀 Project Overview

Objective:
Automate the build, test, and deployment of a simple web application using DevOps best practices — including CI/CD, containerization, monitoring, and security.

Tech Stack:
 🐳 Docker for containerization  
 ⚙️ GitHub Actions for CI/CD  
 ☁️ Render / Railway / AWS EC2 / Cloud Run for deployment  
 📈 Prometheus + Grafana for monitoring  
 🛡️ Trivy for security scanning

---

🧩 Application Details

**Framework:** Python Flask  
**App Output: http://13.233.37.137:8088/

---

CI/CD Pipeline (GitHub Actions):

Workflow File: .github/workflows/deploy.yml

Pipeline Stages:

✅ Checkout code
🔧 Build Docker image
🧪 Test endpoint using curl
🐳 Push image to DockerHub
🚀 Deploy to remote host (via SSH)

---

📊 Monitoring Setup (Prometheus + Grafana)
Prometheus:

Running locally on port 9000
docker run -d -p 9000:9090 --name prometheus prom/prometheus
Verify at: http://localhost:9000/metrics

Grafana:

Running on port 3000
docker run -d -p 3000:3000 --name grafana grafana/grafana
Login: admin / admin
Add Data Source → Prometheus (http://localhost:9000)
Import Dashboard ID: 893 (Docker Monitoring Dashboard)

🛡️ Security Scan (Trivy)

Installed locally:
sudo apt install wget -y
wget https://github.com/aquasecurity/trivy/releases/latest/download/trivy_Linux-64bit.tar.gz
tar -xzf trivy_Linux-64bit.tar.gz
sudo mv trivy /usr/local/bin/


Run the scan:
trivy image drviki-app
