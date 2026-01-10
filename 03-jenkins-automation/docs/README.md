# Project Documentation

## Overview

This project demonstrates setting up a Jenkins CI/CD pipeline using Docker containers with Docker-out-of-Docker (DooD) architecture.

## Prerequisites

- Docker and Docker Compose installed
- Git installed
- Basic understanding of CI/CD concepts

---

## 1. Jenkins Infrastructure Setup

Through the infrastructure diagram below, we can understand how the Jenkins container communicates with our host OS.

![Jenkins Infrastructure](diagrams/jenkins-infrastructure.svg)

## 2. Docker-out-of-Docker (DooD) Sequence

From within the Jenkins container, the Docker CLI sends API requests to the host's Docker daemon via a mounted socket.

![DooD Flow](diagrams/dood-communication-flow.svg)

## 3. Freestyle Job Workflow

This diagram illustrates the continuous integration (CI) process on Jenkins, which pulls code from GitHub and ultimately builds a Docker image.
![Build Workflow](diagrams/freestyle-job-workflow.svg)

## 4. CI/CD Pipeline Roadmap

![Pipeline Roadmap](diagrams/cicd-pipeline-roadmap.svg)

---

## 5. Lesson Notes

[View Lesson Notes](NOTES.md)

---

## 6. Docker Cheatsheet

[View Docker Sheets](DOCKER_CHEATSHEET.md)

---

## 7. How to Run Locally

### Step 1: Create Job

- Click **New Item**
- Enter name and select **Freestyle project**
- Click **OK**

### Step 2: Configure SCM (Git)

- Go to **Source Code Management**
- Select **Git**
- Paste your **Repository URL**
- Set **Branch Specifier** to `*/main`

### Step 3: Configure Build Steps

- Go to **Build Steps** > **Add build step** > **Execute shell**
- Input the following:

```bash
echo "--- Current Directory ---"
pwd
echo "--- Files in Workspace ---"
ls -la
echo "--- Testing Docker Access ---"
docker --version
```

### Step 4: Execute Build

- Click **Save**
- Click **Build Now**
- Check **Console Output** to verify the results.
