# Lab Documentation

## Overview

This lab demonstrates how to make Jenkins automatically build Docker images, tag them with version numbers, push them to Docker Hub, and deploy the containers. Everything is done through shell scripts in Jenkins.

## Prerequisites

- Docker installed and running
- Docker Hub account for pushing images
- Jenkins setup and running
- Git with basic branching (feature, develop, main)
- Basic idea of what CI/CD pipelines do

---

## 1. CI/CD Docker Push Flow

Think of GitHub as the blueprint office where our app plans are kept. Jenkins is the site manager who checks for updated blueprints every few minutes. When he finds new ones, his construction crew (the pipeline stages) builds a Docker "house" from those plans, tests it's solid, then stores it in the Docker Hub warehouse. Finally, the production neighborhood fetches the latest house and opens it for visitors at port 5000. Every code update triggers this whole automatic rebuild-and-replace cycle! This is simplest example to understand this diagram.

![Docker Push Flow](diagrams/cicd-docker-push-flow.svg)

---

## 2. Jenkins DooD Flow

We can imagine our personal computer as a BB house meaning big building, and Docker is the main workshop inside that house area where all the preparations and constructions happen. Meanwhile, Jenkins is like a little manager who lives in a small guest room (the Jenkins container) within it, responsible for managing workflow (CI/CD).

But always remember that Jenkins doesn't have the tools to build things himself! So we give him a walkie-talkie device that's the docker.sock file we mount. Why? Whenever Jenkins needs to build something, for example, when we push code, he will use the walkie-talkie given by us to call the main workshop's foreman (the Docker Daemon) and say, "Hey, build me a Python app with these instructions!"

The foreman says, "Of course, my little manager!" Then, the man creates temporary workbenches (build containers) in the main workshop, runs tests, reports the pass or fail status, and if successful, finally replies back, "Here's your built app, my manager." Jenkins then says, "Thank you, sir! Now push it to the storage shelf (Docker Hub) and put it to work (deploy)!"

![Automation Workflow](diagrams/jenkins-dood-flow.svg)

---

## 3. Docker Tagging Strategy

Think of Git commits as a timeline of snapshots, where each commit captures the exact state of your code and gets a version number. Docker simply takes the latest commit, builds an image from it, tags it with that version, and pushes it to the registry.

![Docker Tagging Strategy](diagrams/docker-tagging-strategy.svg)

---

## 4. Lab Notes

[View Lab Notes](NOTES.md)

---

## 5. Jenkins Lab Cheatsheet

[View Jenkins Lab Sheets](JENKINS_LAB.md)

---

## 6. How to Setup a New Freestyle Project Using Credentials

### Step 1: Create a Freestyle Project

1. Go to your **Jenkins Dashboard** and click **New Item**.
2. Enter the project name: `devops-odyssey-app`.
3. Select **Freestyle project** and click **OK**.

### Step 2: Build Environment (Secure Credentials)

Unlike previous labs, Lab 5 requires secure authentication to push images to Docker Hub.

1. Scroll down to the **Build Environment** section.
2. Check the box **Use secret text(s) or file(s)**.
3. Under **Bindings**, click **Add** and select **Username and Password (separated)**.

- **Username Variable:** `DOCKER_USERNAME`
- **Password Variable:** `DOCKER_PASSWORD`
- **Credentials:** Select the `docker-hub-creds` you can create in Jenkins Credentials settings.

### Step 3: Source Code Management

1. In the **Git** section, enter **Repository URL**: `https://github.com/rubenhtun/devops-odyssey.git` or your own repo.
2. Set the **Branch Specifier** to `*/main`.

### Step 4: Build Steps (Execute Shell)

This is the core of the automation. We move from simple commands to a full Docker lifecycle.

```bash
# Navigate to the specific Lab folder
cd 05-jenkins-docker-push

# Build the Docker Image with a unique Build Number
docker build -t <DOCKER_HUB_USERNAME>/<APP_NAME>:${BUILD_NUMBER} .

# Tag the image as 'latest' for production use
docker tag <DOCKER_HUB_USERNAME>/<APP_NAME>:${BUILD_NUMBER} <DOCKER_HUB_USERNAME>/<APP_NAME>:latest

# Login to Docker Hub using Non-Interactive Mode
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin

# Push both Versioned and Latest images to the Registry
docker push <DOCKER_HUB_USERNAME>/<APP_NAME>:${BUILD_NUMBER}
docker push <DOCKER_HUB_USERNAME>/<APP_NAME>:latest

# Cleanup old containers and run the new version
docker rm -f <CONTAINER_NAME> || true
docker run -d --name <CONTAINER_NAME> -p 5000:5000 <DOCKER_HUB_USERNAME>/<APP_NAME>:latest
```
