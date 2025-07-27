 #                                                        CI/CD for a Python (Flask) App
## 🔹 Project Introduction

This project implements a fully automated **CI/CD pipeline** for a Python Flask web application. It integrates key DevOps tools and services:

- **GitHub** for version control  
- **GitHub Actions** for Continuous Integration (CI)  
- **Jenkins** for Continuous Deployment (CD)  
- **Docker** for containerization  
- **AWS EC2** for hosting the final deployment  

The project enables developers to build, test, and deploy their Flask application automatically on code changes.
 <br> <br>
## 🔹 Architecture diagram

<img width="512" height="768" alt="image" src="https://github.com/user-attachments/assets/afd7e509-c269-4092-8bb8-18c9d8420e48" />
 <br> <br>
 
## 🔹 Tech stack

| Layer              | Tools           |
|--------------------|-----------------|
| Source Control     | Git + GitHub    |
| App Framework      | Python Flask    |
| CI                 | GitHub Actions  |
| CD                 | Jenkins         |
| Containerization   | Docker          |
| Deployment         | AWS EC2         |
| Testing            | Pytest, Flake8  |
   
## 🔹 Setup instructions (local and Jenkins)

## 🔧 Local Setup
Follow these steps to run the Flask app and test the CI pipeline locally:

### 1. Clone the Repository
git clone https://github.com/your-username/your-repo.git <br>
cd your-repo

### 2\. (Optional) Create and Activate Virtual Environment

python \-m venv venv
source venv/bin/activate  \# On Windows: venv\\Scripts\\activate

### 3\. Install Dependencies

pip install \-r requirements.txt

### 4\. Lint and Test the Code

flake8 .
pytest

### 5\. Run the App Locally

python app.py  <br>
\# Or using Docker <br>
docker build \-t flask-app-image .  <br>
docker run \-d \-p 5000:5000 flask-app-image

## ⚙️ CI Setup using GitHub Actions
CI is implemented using GitHub Actions to ensure clean code and passing tests before deployment.

**Workflow Location:**  
`.github/workflows/ci.yml`

**Workflow Tasks:**
 *   ✅ Lint Python code with flake8   
 *   ✅ Run unit tests with pytest   

**Triggers:**

 *   On every push and pull\_request to any branch    

**Outcome:**

 *   Ensures code quality     
 *   Avoids breaking changes before reaching production   

## 🔁 CD Setup using Jenkins + Docker

CD is managed with Jenkins, hosted via Docker Desktop container.

### Jenkins Setup:
 *  Installed Jenkins via Docker Desktop     
 *   Installed Git inside Jenkins container     
 *   Installed required Jenkins plugins:    
     *   Git   
     *   Docker
     *   SSH Agent    
     *   Pipeline    

### Ngrok for Webhooks:

*    Exposed Jenkins via ngrok HTTPS tunnel    
*    Used ngrok public HTTPS URL in GitHub Webhooks    

### Pipeline Automation:

Created `Jenkinsfile` with the following stages:

 1.  Clone repository     
 2.  Build Docker image    
 3.  SSH into AWS EC2 instance     
 4.  Stop and remove old container (if any)     
 5.  Build and run new Docker container on EC2    

## ☁️ AWS EC2 Deployment

The Flask app is deployed on an AWS EC2 instance with Docker.

### EC2 Setup:

 *   Launched a t2.micro EC2 instance    
 *   Installed Docker    

### Jenkins to EC2 SSH Integration:

 *   Configured Jenkins with private key using SSH Agent     
 *   Jenkins uses SSH to access EC2 and run deployment commands    

### Automated Deployment on Code Push:

 1.  Jenkins pipeline triggers on push to main     
 2.  SSH into EC2    
 3.  Pulls latest code, removes old container/image     
 4.  Builds and runs new Docker container with updated Flask app     

##  Final Deployment Output

Access your Flask app in the browser at:

http://<your-ec2-public-ip\>/

The application will show the Dashboard and Status APIs with full CI/CD automation.

<br> <br>

# 🔹 Sample API response
## Home Page ( / )
<img width="1844" height="847" alt="flask api " src="https://github.com/user-attachments/assets/00944b38-12d3-4fb9-b25e-282cae5394d4" />
<br> <br> 

## Status Page  ( /status )
<img width="1842" height="825" alt="Screenshot (716)" src="https://github.com/user-attachments/assets/a5f25d75-f6ce-4351-b53f-c83f1ef94982" />
<br> <br>

# 🔹 Screenshots of each pipeline stage
 <img width="1854" height="867" alt="Screenshot (722)" src="https://github.com/user-attachments/assets/cadd9190-7418-4755-a161-c5313913b792" />
 <br> <br>
<img width="1849" height="871" alt="Screenshot (708)" src="https://github.com/user-attachments/assets/5421350c-2fc0-403b-a623-26d3c5ecaf09" />
 <br> <br>
<img width="1827" height="814" alt="Screenshot (712)" src="https://github.com/user-attachments/assets/c70f63f1-389e-45ac-ab5a-a114870d27d6" />
 <br> <br>
<img width="1806" height="852" alt="image" src="https://github.com/user-attachments/assets/88c5b916-e438-43f2-9711-8783548722de" />
 <br> <br>
 
# 🔹 GitHub Action & Jenkins output
   <img width="1849" height="897" alt="Screenshot (724)" src="https://github.com/user-attachments/assets/b2e94adb-119d-4991-985c-9108fc9c7ceb" />
 <br> <br>
<img width="1841" height="867" alt="Screenshot (707)" src="https://github.com/user-attachments/assets/40f925bc-0b04-413e-9f92-dfee821f0bb0" />
 <br> <br>
<img width="1853" height="875" alt="Screenshot (713)" src="https://github.com/user-attachments/assets/e51148c1-0bb4-4373-b05e-05dc6998f5b3" />
 <br> <br>
<img width="1844" height="853" alt="Screenshot (714)" src="https://github.com/user-attachments/assets/44eb3fa7-5951-4e94-89a2-b93adf2ad6a1" />
 <br> <br>
 
# 🔹 AWS EC2 access & output screenshot
 <br> <br>
  <img width="1855" height="820" alt="Screenshot (717)" src="https://github.com/user-attachments/assets/35812d97-eaec-48cb-9c90-f8a166275c03" />
 <br> <br>
<img width="1811" height="424" alt="Screenshot (720)" src="https://github.com/user-attachments/assets/26608eff-c18d-4722-9883-45b0cbbbf2e9" />
 <br> <br>
<img width="1869" height="978" alt="Screenshot (719)" src="https://github.com/user-attachments/assets/ae8a851d-25e8-496d-a6da-9711a2d94281" />
 <br> <br>




