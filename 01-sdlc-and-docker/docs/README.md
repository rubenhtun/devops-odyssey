# Lab Documentation

## Overview

This is a practical DevOps learning lab demonstrating SDLC (Software Development Life Cycle)
principles implemented through Docker containerization. The hands-on session provides practical working examples of manual Docker workflows, automated scripting in `deploy.sh`, and multi-service orchestration using Docker Compose.

## Prerequisites

- Docker & Docker Compose installed and running on local machine or server
- Basic Linux knowledge and familiarity with terminal commands
- Simple Flask Python application that returns small HTML view
- PostgreSQL for database connection as a Docker Compose part
- Created `deploy.sh` script for one-command deployment

---

## 1. SDLC Flowchart

We can easily think of SDLC like a simple sequential process from developing software and fixing vulnerabilities from scratch, stage to a final polished product - it needs ongoing maintenance though. Basically, it includes eight essential steps every real-world app goes through, from figuring and collecting various sorts of requirements, operation to work properly, and more improvements on it through requesting suggestions from end users.

![SDLC Flowchart](diagrams/sdlc-flowchart.svg)

---

## 2. Manual Docker Build & Run Workflow

So next what exactly happens when we run `docker build` and `docker run` in the local terminal? Here, we can think of it like building crafted Lego toys. First, we need a base image as our foundation like a Lego baseplate. The same applies in this workflow either. We download essential environment parts of an app including base image, namely like `python:3.9-slim`, then add layers by installing dependencies from `requirements.txt` file, and finally assemble everything into a runnable container on our local machine.

![Manual Docker Build & Run](diagrams/docker-manual-build-run-flow.svg)

---

## 3. Manual Docker Script Flow

In this diagram, an alternative-driven approach is shown, providing an easy-peasy and worthwhile impact on the entire workflow. Within a shell script, we collect all messy Docker commands, avoiding the need to typing them one line after another. In a dark terminal, a single command, `./deploy.sh`, does everything in a defined order: it stops the old container, removes it, builds a new image, and starts a new container again.

It's like having a personal assistant for deployments! Lol!!!

![Docker Script Flow](diagrams/docker-manual-script-flow.svg)

---

## 4. Docker Compose Multi-Service Workflow

In software development, almost every single isolated service cannot exist on its own. Contrary to this, at least, they have to rely on other essential services, much like living in a union. In the same way, our app also needs other friends, such like a database, to work together. Here, `Docker Compose` becomes the team manager triggers shared collaboration among them.

Thus, this diagram highlights how it coordinates the web app and database, sets up a core relationship through private networks, and ensures they can communicate with each other based on their respective requirements.

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
