# 🚀 Flask + MySQL Dockerized Application with Jenkins CI/CD

A containerized multi-tier web application built with **Flask**, **MySQL**, and **Docker Compose**, integrated with an automated **Jenkins CI/CD pipeline** powered by **Docker-as-Agent architecture**.

> ⭐ **Key Highlight:** This project doesn't just use Docker to containerize the application — it also uses **Docker containers as dynamic Jenkins build agents**, meaning every pipeline run spins up a fresh, isolated container to execute the build, and automatically destroys it once the job completes. No permanently running worker nodes, no manual dependency management.

## 📌 Project Overview

This project demonstrates a complete DevOps workflow — from local development to automated build and delivery:
- A Flask web application connected to a MySQL database
- Fully containerized using Docker and orchestrated with Docker Compose
- An automated CI/CD pipeline in Jenkins that triggers a build, packages the app into a Docker image, and pushes it to Docker Hub
- **Jenkins pipeline execution happens entirely inside dynamically created Docker containers** — the core DevOps concept this project showcases

## 🐳 Docker-as-Agent: The Core of This Project

Most beginner CI/CD setups run Jenkins pipelines directly on the Jenkins host machine. This project instead implements the **industry-standard Docker-as-Agent pattern**, which is how modern organizations scale Jenkins for microservices:

- **No static worker nodes.** Traditional Jenkins setups require pre-configured EC2/VM worker nodes that stay running 24/7, need manual software installs, and cause version/dependency conflicts between teams.
- **Ephemeral, on-demand agents.** In this setup, Jenkins spins up a temporary Docker container (`docker:latest` image) *only when a pipeline runs*, executes all stages inside it, and automatically tears it down when the build finishes — success or failure.
- **Docker socket binding.** The container is given controlled access to the host's Docker daemon via `-v /var/run/docker.sock:/var/run/docker.sock`, allowing it to build and push images without needing Docker installed inside the container itself.
- **Secure, least-privilege access.** Instead of running the agent container as `root` (a common but insecure shortcut), this pipeline uses `--group-add` with the host's Docker group GID — granting the container just enough permission to access the Docker socket, following the principle of least privilege.
- **Scoped credential handling.** Docker Hub credentials are injected only within the specific stage that needs them using `withCredentials`, rather than being exposed pipeline-wide.

### Why this matters
This approach is significantly more **cost-efficient** (no idle servers), more **consistent** (every build starts from a clean environment), and easier to **maintain** (updating a tool version is a one-line image tag change, not a manual server update). It's the same pattern used by companies running large-scale microservices CI/CD.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Python (Flask) |
| Database | MySQL 8.0 |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI/CD | Jenkins (Pipeline as Code, Docker-as-Agent) |
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
│ dynamically spins up
▼
┌─────────────────────────┐
│ Temporary Docker Agent │
│ Container (auto-destroyed) │
│ ───────────────────────── │
│ 1. Checkout code from Git │
│ 2. Build Docker image │
│ 3. Authenticate + push │
│ to Docker Hub │
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
├── Jenkinsfile # CI/CD pipeline (Docker-as-Agent architecture)
└── README.md

## ⚙️ Key Features

- **Multi-container application** — web app and database run as isolated, networked services
- **Persistent storage** — MySQL data stored in a Docker volume, surviving container restarts
- **Docker-as-Agent CI/CD** — pipeline runs inside ephemeral, auto-destroyed Docker containers instead of static worker nodes
- **Least-privilege container access** — Docker socket access granted via group membership, not root
- **Scoped secrets management** — Docker Hub credentials injected only where needed via Jenkins' `withCredentials`
- **Custom, responsive UI** — clean interface built with vanilla HTML/CSS

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

## 🔄 CI/CD Pipeline Stages

1. **Checkout** — Pulls the latest code from the GitHub repository
2. **Build Docker Image** — Builds a Docker image of the Flask application, executed inside a freshly spun-up Docker agent container
3. **Login & Push to Docker Hub** — Authenticates using Jenkins-scoped credentials and publishes the image to Docker Hub

Every run creates a new agent container from scratch and destroys it on completion — no leftover state, no configuration drift between builds.

## 🎯 What I Learned

- Setting up Jenkins and configuring **Docker as a dynamic, ephemeral build agent** (rather than static worker nodes)
- Solving real-world Docker-in-Jenkins issues: Docker socket permission errors, container `HOME` directory permission failures, and entrypoint/container startup issues
- Applying **least-privilege security practices** to CI/CD agents using `--group-add` instead of defaulting to root
- Securely scoping secrets in Jenkins pipelines using `withCredentials`
- Understanding the trade-offs between traditional static worker nodes vs. Docker-as-Agent architecture, and when each is appropriate
- Writing Dockerfiles and orchestrating multi-container apps with Docker Compose

## 🔮 Future Improvements

- Deploy the application to AWS EC2 within a custom VPC
- Add Nginx as a reverse proxy for production-grade traffic handling
- Integrate SonarQube for automated code quality checks in the pipeline
- Add Prometheus and Grafana for monitoring and alerting
- Implement an automated testing stage before build/push

---

**Author:** Shahbaz Ali
**Role:** DevOps Enthusiast | Cloud & Automation
