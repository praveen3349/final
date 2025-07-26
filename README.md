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

# CI/CD Pipeline for Flask Application

## Technology Stack

| Layer              | Tools           |
|--------------------|-----------------|
| Version Control    | GitHub          |
| Application        | Python Flask    |
| CI                 | GitHub Actions  |
| CD                 | Jenkins         |
| Containerization   | Docker          |
| Deployment         | AWS EC2         |
| Testing            | Pytest, Flake8  |

## Key Features

### Dockerized Flask App
- Health check endpoint
- Consistent environments
- Port 5000 exposed

### GitHub Actions CI
- Automatic linting with flake8
- Unit testing with pytest
- Triggered on push/PR to main branch

### Jenkins CD Pipeline
- Docker image building
- EC2 deployment via SSH
- Automated container management

### Automated Testing
- Unit tests run in both CI/CD
- Fail-fast validation
- Test coverage reporting

## Pipeline Workflow

1. **Code Commit**  
   Developer pushes code → GitHub

2. **CI Phase (GitHub Actions)**  
   - Code linting (flake8)  
   - Unit tests (pytest)  
   ![CI Pipeline](https://img/gh-actions.png)

3. **CD Phase (Jenkins)**  
   - Builds Docker image  
   - Pushes to container registry  
   - Deploys to EC2 via SSH  
   ![CD Pipeline](https://img/jenkins-output.png)

4. **Deployment**  
   - Container runs on EC2  
   - Port mapping: 5000→80  
   ![Running App](https://img/app-running.png)

## Setup Instructions

### Prerequisites
- GitHub account
- AWS EC2 access
- Jenkins server (v2.4+)
- Docker installed
- Python 3.9+

### Configuration Steps
1. **EC2 Setup**
   - Launch t2.micro instance
   - Configure security groups:
     - HTTP (80)
     - SSH (22)
   - Install Docker

2. **Jenkins Configuration**
   - Install required plugins:
     - Docker Pipeline
     - SSH Agent
     - GitHub Integration
   - Configure AWS credentials

3. **Pipeline Setup**
   - Connect GitHub repo
   - Set up webhooks
   - Configure deployment scripts

## AWS Infrastructure

| Component        | Specification           |
|------------------|-------------------------|
| Instance Type    | t2.micro                |
| OS               | Ubuntu 22.04 LTS        |
| Docker Version   | 20.10+                  |
| Security Groups  | HTTP (80), SSH (22)     |
| Storage          | 8GB EBS                 |
