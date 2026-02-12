# Lab 01: SDLC & Docker Basics

## What This Lab Is About

As a developer, I crave doing practical things to grasp nested concepts through experience, and that's accounted for. So as you know, the first step in anything new in our life seems awkward to everyone. Right? But we are always supposed to seek alternative approaches to critically solve problems through a self-constructive mindset.

And then, frankly saying that one of my passionate habits is going to deep dive into system architecture and building. Therefore, to an extent, some amount of experiments in terms of DevOps mini series of labs using Docker and Jenkins tools are conducted based on my authentic decision.

First of all, I came to understand the software development lifecycle with sequential processes easily leads to fully completed and systematic software that reaches end users. Especially I got a great chance to learn how containers solve the "works on my machine" problem.

---

## Quick Cheat Sheet

### Core Ideas

- **SDLC**: In short, there are a minimum of eight steps in the Software Development Life Cycle.
- **Docker**: What Docker do? My pov is it easily packages software apps with their related environment so they can run anywhere.
- **Docker Compose**: Normally, containers tend to rely on each other to fully operate an app. So for that reason, Docker Compose manages multiple containers that need to work together.
- **Port Mapping**: About this, my metaphorical understanding is that connecting my computer to containers is like doors between rooms.

---

### Commands I Used

```bash
# Stop existing container
docker stop <CONTAINER_ID_OR_NAME> || true

# Remove existing container
docker rm <CONTAINER_ID_OR_NAME> || true

# Build from Dockerfile
docker build -t <APP_NAME> .

# Run a container
docker run -d --name <CONTAINER_ID_OR_NAME> -p 3000:5000 <APP_NAME>

# Docker Compose magic
docker-compose up -d
docker-compose down

# See what's running
docker ps
docker-compose ps
```

---

### My Setup

- **Tools**: Docker, Docker Compose, Git
- **App**: Flask Python application
- **Database**: PostgreSQL
- **Automation**: Created `deploy.sh` script for one command line deployment

---

## Here's What I Actually Did

### Step 1: Understand SDLC (The Big Picture)

**Action**: Initially, learned the eight stages of software development.  
**How**: From "Requirements" gathering to ongoing "Operation" and "Feedback".  
**Why**: The reason to understand what specific parts we can automate in the development process with the help of DevOps tools.

### Step 2: Build First Docker Container

**Action**: Created a Dockerfile and built a Flask app image.  
**How**: Defined a Python environment, installed Flask, packaged everything in a single folder.  
**Why**: Finally, my app runs the same everywhere and no more "works on my machine" issue, good news, right?

### Step 3: Run & Manage Containers

**Action**: Started containers, mapped ports, checked logs.  
**How**: Used regular `docker run`, `docker ps`, `docker logs` commands.  
**Why**: To actually apply the containers I built and debug in case something is broken.

### Step 4: Automate with Scripts

**Action**: Easy peasy, separated additional `deploy.sh` for one short command line deployments.  
**How**: Listed multiple Docker commands into a single script file.  
**Why**: Because it saves time and avoids mistakes from typing hard-coded commands manually.

### Step 5: Orchestrate with Docker Compose

**Action**: Built a bridge to set up Flask app + PostgreSQL database together.  
**How**: Created `docker-compose.yml` with services and networks as needed.
**Why**: Real apps usually need multiple components working together.

---

**Pro tip:** Check out the [Docker Cheatsheet](DOCKER_CHEATSHEET.md) if you forget any commands!
