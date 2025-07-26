# CI/CD Pipeline for Flask Application

---

## Project Overview
**Objective**:  
Fully automated CI/CD pipeline for Python Flask web application  

**Key Components**:
- GitHub (Version Control)
- GitHub Actions (CI)
- Jenkins (CD)
- Docker (Containerization)
- AWS EC2 (Deployment)

---

## Architecture Diagram
```plaintext
[GitHub Repository]
       ↓
[GitHub Actions CI (Linting + Testing)]
       ↓
[Jenkins CD Pipeline (Build → Docker → Deploy)]
       ↓
[AWS EC2 Instance (Running Containerized Flask App)]
