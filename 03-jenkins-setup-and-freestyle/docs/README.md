# Lab Documentation

## Overview

If saying in an articulated way, a Jenkins CI/CD pipeline is a continuous, automated process, particularly focused on boosting development agility using Docker containers and orchestration. In this lab, Docker-out-of-Docker is the main key feature to learn about, and what it is used for. Moreover, some hands-on work, like environment setup, launching the container, unlocking Jenkins, initial configuration, and installing the Docker CLI inside Jenkins are covered, but it's just so-so.

## Prerequisites

- Docker and Docker Compose installed
- Git installed
- Basic understanding of CI/CD concepts

---

## 1. Jenkins Infrastructure Setup

As we see, the developer must communicate with the host machine os to see the Jenkins dashboard interface via a port number. Jenkins server container running in Docker Engine always tries to build other containers relying on socket mounting like a tunnel, and saves persistent volume data into the Jenkins home folder.

![Jenkins Infrastructure](diagrams/jenkins-infrastructure.svg)

---

## 2. Docker-out-of-Docker (DooD) Sequence

Next step, going into details a bit, the Docker CLI from within the Jenkins container sends API requests to the host's Docker daemon via a mounted socket. Like already explained before, socket two-way communicator serves as a medium catalyst to forward Docker Daemon, where main executions occur, and backward Docker CLI to show final results.

![DooD Flow](diagrams/dood-communication-flow.svg)

---

## 3. Freestyle Job Workflow

Be brave for repetitions. And be brave for the little unknown. Now our focus is on how Jenkins actually does the work. When we trigger a tangible click on the "build" button, the autopilot, Jenkins make auto awakening of a freestyle job. First step, reach out to there, GitHub to pull all the latest source code into its workspace and download it. After that, Jenkins starts multiple remaining build steps as configured in the job. The steps include running tests, compiling code, building a Docker image, push image to Docker Hub, and so on. Finally, it cleans up workspace for the next build and sends notifications to the developer.
![Build Workflow](diagrams/freestyle-job-workflow.svg)

---

## 4. CI/CD Pipeline Roadmap

After reading all the above, you may wonder what's next? But don't worry because this is just a simple CI/CD pipeline roadmap. In the next labs, you will learn more about how this pipeline stages work in detail through hard codes line by line.
![Pipeline Roadmap](diagrams/cicd-pipeline-roadmap.svg)

---

## 5. Lab Notes

[View Lab Notes](NOTES.md)

---

## 6. Jenkins Cheatsheet

[View Jenkins Cheatsheet](JENKINS_LAB.md)

---

## 7. How to Run Locally

### Step 1: Create Freestyle Project

- Click **New Item**
- Enter name and select **Freestyle project**
- Click **OK**

### Step 2: Configure SCM (Git)

- Go to **Source Code Management**
- Select **Git**
- Paste **Repository URL**
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

---

## 8. Extra Tips

- **Automated Builds:** To enable automatic builds, check the **Poll SCM** option in the build trigger section.
- **Polling Schedule:** Add `* * * * *` in the **Schedule** field to instruct Jenkins to check GitHub every minute.
- **Effect:** This ensures Jenkins automatically detects new commits, keeping the workspace and pipeline synchronized with the latest code changes.
