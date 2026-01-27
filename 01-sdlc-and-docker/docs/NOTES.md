# Lab 01: SDLC & Docker Basics

## What This Lab Is About

Noticeably, to understand that following the software development lifecycle with sequential processes easily leads to fully completed and systematic software that reaches end users. Mainly learned how containers solve the "works on my machine" problem.

---

## Here's What I Actually Learned

### 1. SDLC Fundamentals

- Learned the 8 stages: Requirements, Design, Development, Build, Test, Deploy, Operate, and Feedback.
- Understanding the **Software Development Life Cycle** is the foundation for CI/CD automation.

### 2. Programming Languages in DevOps

- **Compiled (Java, Go):** Need to be built into artifacts before running.
- **Interpreted (Python, Node.js):** Run directly via an interpreter but require specific runtime environments.

### 3. Containerization (Docker)

- **Dockerfile:** Used to define the environment, install dependencies, and package the application.
- **Artifacts:** Created a portable Docker Image that contains everything the app needs to run.
- **Container:** Actual running application of that image

### 4. Orchestration & Networking (Docker Compose)

- Used **Docker Compose** to manage multi-container setups.
- Implemented **Virtual Networking** to allow the Web container and Database container (Postgres) to communicate.
- Learned about **Port Mapping** (`3000:5000`) and **Environment Variables**.

---

### Commands I Used

```bash
# Stop existing container
docker stop devops-odyssey-app || true

# Remove existing container
docker rm devops-odyssey-app || true

# Build from Dockerfile
docker build -t python-app .

# Run a container
docker run -d --name devops-odyssey-app -p 3000:5000 python-app

# Docker Compose magic
docker-compose up -d
docker-compose down

# See what's running
docker ps
docker-compose ps
```

**Bonus:** I automated all these commands in a `deploy.sh` script for easy reuse!
