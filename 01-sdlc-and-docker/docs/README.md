# Lab Documentation

## Overview

This is a practical DevOps learning lab demonstrating SDLC (Software Development Life Cycle)
principles implemented through Docker containerization. The hands-on session provides working examples of manual Docker workflows, automated scripting, and multi-service orchestration using Docker Compose.

## Prerequisites

- Docker & Docker Compose installed and running on local machine or server
- Basic Linux knowledge and familiarity with terminal commands
- Simple Flask Python application (returns HTML)
- PostgreSQL for database connection (for Docker Compose part)
- Created `deploy.sh` script for one-click deployment

---

## 1. SDLC Flowchart

We can easily think of SDLC like a recipe for building software from scratch to finished product. Basically, it shows the eight essential steps every app goes through, from figuring out what to build (Requirements) to keeping it running (Operate) and improving it (Feedback).

![SDLC Flowchart](diagrams/sdlc-flowchart.svg)

---

## 2. Manual Docker Build & Run Workflow

So what exactly happens when we run `docker build` and `docker run` in terminal? Think of it like robotics development. Similarly, in this workflow, we download the parts such as base image like `python:3.9-slim`, assemble them through additional installation of dependencies from `requirements.txt`, then set up the finished app (run container) on our local computer.

![Manual Docker Build & Run](diagrams/docker-manual-build-run-flow.svg)

---

## 3. Manual Docker Script Flow

This diagram shows how we automated the boring parts with a shell script. One command `./deploy.sh` does: stop old container, remove it, build new image, start new container again. It's like having a personal assistant for deployments! Lol!!!

![Docker Script Flow](diagrams/docker-manual-script-flow.svg)

---

## 4. Docker Compose Multi-Service Workflow

When our app needs friends like a database, `Docker Compose` becomes the team manager for collaboration. This diagram shows how it coordinates the web app and database, sets up their private chat network, and makes sure they can talk to each other while being isolated from the outside world.

![Docker Compose Flow](diagrams/docker-compose-app-flow.svg)

---

## 5. Lab Notes

[View Lab Notes](NOTES.md)

---

## 6. Docker Cheatsheet

[View Docker Sheets](DOCKER_CHEATSHEET.md)

---

## 7. How to Run Locally

```bash
git clone https://github.com/rubenhtun/devops-odyssey.git
```

```bash
cd devops-odyssey/01-sdlc-and-docker
```

```bash
chmod +x deploy.sh
```

```bash
./deploy.sh
```

### or

```bash
bash deploy.sh
```
