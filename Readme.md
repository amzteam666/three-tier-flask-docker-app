# 🚀 Flask + MySQL Dockerized Application with Jenkins CI/CD

A containerized multi-tier web application built with **Flask**, **MySQL**, and **Docker Compose**, integrated with an automated **Jenkins CI/CD pipeline** that builds and pushes Docker images to Docker Hub using **Docker-as-Agent** architecture.

## 📌 Project Overview

This project demonstrates a complete DevOps workflow — from local development to automated build and delivery:
- A Flask web application connected to a MySQL database
- Fully containerized using Docker and orchestrated with Docker Compose
- An automated CI/CD pipeline in Jenkins that triggers on code changes, builds a Docker image, and pushes it to Docker Hub
- Jenkins pipeline runs inside **dynamically created Docker containers** (Docker-as-Agent), rather than relying on permanently running worker nodes

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Python (Flask) |
| Database | MySQL 8.0 |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI/CD | Jenkins (Pipeline as Code) |
| Image Registry | Docker Hub |
| Version Control | Git & GitHub |
| OS Environment | Ubuntu (Linux) |

## 🏗️ Architecture

┌──────────────┐ git push ┌──────────────┐
│ Developer │ ───────────────> │ GitHub │
└──────────────┘ └───────┬───────┘
│ triggers
▼
┌───────────────────┐
│ Jenkins Server │
│ (Docker installed) │
└─────────┬───────────┘
│ spins up
▼
┌─────────────────────────┐
│ Temporary Docker Agent │
│ Container (auto-deleted) │
│ - Checkout code │
│ - Build Docker image │
│ - Push to Docker Hub │
└─────────────┬─────────────┘
│
▼
┌───────────────────┐
│ Docker Hub │
│ (Image Registry) │
└───────────────────┘


## 📂 Project Structure

flask-docker-app/
├── app/
│ ├── app.py # Flask application logic
│ ├── Dockerfile # Container build instructions for the app
│ └── requirements.txt # Python dependencies
├── docker-compose.yml # Multi-container orchestration config
├── Jenkinsfile # CI/CD pipeline definition (Docker-as-Agent)
└── README.md


## ⚙️ Key Features

- **Multi-container application**: Web app and database run as isolated, networked services
- **Persistent storage**: MySQL data stored in a Docker volume, surviving container restarts
- **Environment-based configuration**: Credentials and configs passed via environment variables
- **Automated CI/CD pipeline**: Every code change can trigger an automated build and push to Docker Hub
- **Docker-as-Agent Jenkins architecture**: Pipeline runs inside temporary, isolated Docker containers instead of static, always-on worker nodes — reducing cost and eliminating dependency conflicts
- **Secure credential handling**: Docker Hub credentials managed via Jenkins Credentials Store, scoped only to the stages that need them
- **Custom, responsive UI**: Clean interface built with vanilla HTML/CSS

## 🚀 How to Run Locally

1. Clone the repository:
```bash
   git clone https://github.com/amzteam666/three-tier-flask-docker-app.git
   cd three-tier-flask-docker-app
```

2. Build and start the containers:
```bash
   docker compose up --build
```

3. Open your browser and navigate to:

http://localhost:5000


4. To stop the application:
```bash
   docker compose down
```

## 🔄 CI/CD Pipeline Overview

The Jenkins pipeline (`Jenkinsfile`) automates the following stages:

1. **Checkout** — Pulls the latest code from the GitHub repository
2. **Build Docker Image** — Builds a Docker image of the Flask application
3. **Login to Docker Hub** — Authenticates securely using Jenkins-stored credentials
4. **Push to Docker Hub** — Publishes the built image to Docker Hub for use in deployment

The entire pipeline runs inside a **temporary Docker agent container**, which is created fresh for every build and automatically destroyed once the pipeline completes — ensuring a clean, consistent, and cost-efficient build environment.

## 🎯 What I Learned

- Writing Dockerfiles and orchestrating multi-container apps with Docker Compose
- Managing inter-container networking and persistent volumes
- Setting up Jenkins and configuring it to use Docker as a dynamic build agent
- Solving real-world DevOps issues such as Docker socket permissions and credential scoping in Jenkins pipelines
- Securely managing secrets using Jenkins Credentials Store and `withCredentials`
- Understanding the trade-offs between traditional static worker nodes vs. Docker-as-Agent architecture

## 🔮 Future Improvements

- Deploy the application to AWS EC2 within a custom VPC
- Add Nginx as a reverse proxy for production-grade traffic handling
- Integrate SonarQube for automated code quality checks in the pipeline
- Add Prometheus and Grafana for monitoring and alerting
- Implement automated testing stage before build/push

---

**Author:** Shahbaz Ali
**Role:** DevOps Enthusiast | Cloud & Automation
