# 🚀 CI/CD for a Python (Flask) App

## 🔹 Project Introduction

This project implements a fully automated **CI/CD pipeline** for a Python Flask web application. It integrates key DevOps tools and services:

- **GitHub** for version control  
- **GitHub Actions** for Continuous Integration (CI)  
- **Jenkins** for Continuous Deployment (CD)  
- **Docker** for containerization  
- **AWS EC2** for hosting the final deployment  

The project enables developers to build, test, and deploy their Flask application automatically on code changes.

---

## 🔹 Architecture Diagram

```mermaid
flowchart TD
    A[Developer Push to GitHub] --> B[GitHub Actions - CI]
    B --> C[Lint with flake8]
    B --> D[Run Unit Tests (pytest)]
    D --> E[Jenkins - CD]
    E --> F[Build Docker Image]
    F --> G[Push to EC2 (via SSH)]
    G --> H[Docker Run Container]
    H --> I[Flask App Running on EC2]


## Technology Stack
 _______________________________________
| Layer              | Tools           |
|--------------------|-----------------|
| Version Control    | GitHub          |
| Application        | Python Flask    |
| CI                 | GitHub Actions  |
| CD                 | Jenkins         |
| Containerization   | Docker          |
| Deployment         | AWS EC2         |
| Testing            | Pytest, Flake8  |
|____________________|_________________|
