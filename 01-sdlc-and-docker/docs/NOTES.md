# Lab 01: SDLC & Docker Basics

## What This Lab Is About

Noticeably, to understand that following the software development lifecycle with sequential processes easily leads to fully completed and systematic software that reaches end users. Mainly learned how containers solve the "works on my machine" problem.

---

## Quick Cheat Sheet

### Core Ideas

- **SDLC**: The 8-step journey from idea to working software
- **Docker**: Packaging apps with their environment so they run anywhere
- **Docker Compose**: Managing multiple containers that need to work together
- **Port Mapping**: Connecting my computer to containers like doors between rooms

### Commands I Used

```bash
# Stop existing container
docker stop <container-name> || true

# Remove existing container
docker rm <container-name> || true

# Build from Dockerfile
docker build -t <app-name> .

# Run a container
docker run -d --name <container-name> -p 3000:5000 <app-name>

# Docker Compose magic
docker-compose up -d
docker-compose down

# See what's running
docker ps
docker-compose ps
```

### My Setup

- **Tools**: Docker, Docker Compose, Git
- **App**: Simple Flask Python application
- **Database**: PostgreSQL for the multi-container part
- **Automation**: Created `deploy.sh` script for one-click deployment

## Here's What I Actually Did

### Step 1: Understand SDLC (The Big Picture)

**Action**: Learned the 8 stages of software development  
**How**: From Requirements gathering to ongoing Operation and Feedback  
**Why**: To understand what parts we're automating with DevOps tools

### Step 2: Build My First Docker Container

**Action**: Created a Dockerfile and built a Flask app image  
**How**: Defined Python environment, installed Flask, packaged everything  
**Why**: So my app runs the same everywhere and no more "works on my machine" issue

### Step 3: Run & Manage Containers

**Action**: Started containers, mapped ports, checked logs  
**How**: Used `docker run`, `docker ps`, `docker logs` commands  
**Why**: To actually use the containers I built and debug when needed

### Step 4: Automate with Scripts

**Action**: Created `deploy.sh` for one-click deployments  
**How**: Combined multiple Docker commands into a single script  
**Why**: Save time and avoid mistakes from typing commands manually

### Step 5: Orchestrate with Docker Compose

**Action**: Set up Flask app + PostgreSQL database together  
**How**: Created `docker-compose.yml` with services and networks  
**Why**: Real apps usually need multiple components working together

---

**Pro tip:** Check out the [Docker Cheatsheet](DOCKER_CHEATSHEET.md) if you forget any commands!
