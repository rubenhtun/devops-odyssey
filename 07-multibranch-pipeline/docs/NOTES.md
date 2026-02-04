# Lab 07: Jenkins Multibranch Pipeline

## What This Lab Is About

In Lab 06, we automated a single `main` branch. In Lab 07, we leveled up to a **Multibranch Pipeline**. This allows Jenkins to automatically scan my GitHub repository, discover all active branches (**main, develop, feature-login**), and automatically create a dedicated pipeline for each one. We also implemented **Dynamic Port Mapping** to run all branch environments simultaneously without port conflicts.

---

## Quick Cheat Sheet

### Core Ideas

- **Monorepo Strategy**: Organizing code and configuration files within sub-folders systematically.
- **Automatic Branch Indexing**: Jenkins scans the repo and turns any branch containing a `Jenkinsfile` into an active pipeline.
- **Dynamic Port Mapping**: Assigning different ports (5000, 5001, 5002) based on the branch name for concurrent deployments.
- **Docker Layer Caching**: Optimizing the `Dockerfile` by installing dependencies before copying the full app code to speed up builds.

### Commands I Ran (Inside the Jenkinsfile)

```groovy
// Make dynamic ports depending on GitHub repo branches
def PORT_MAP = ['main': 5000, 'develop': 5001, 'feature-login': 5002]
def DEPLOY_PORT = PORT_MAP.get(env.BRANCH_NAME) ?: 5003

// Build Docker image into a specific sub-folder
dir('07-multibranch-pipeline') {
    sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
}

// Deployment with specific environment variables
sh """
    docker run -d --name ${CONTAINER_NAME} \
    -p ${DEPLOY_PORT}:5000 \
    -e BRANCH_NAME=${env.BRANCH_NAME} \
    -e BUILD_NUMBER=${env.BUILD_NUMBER} \
    ${DOCKER_IMAGE}:${IMAGE_TAG}
"""
```

### My Setup

- **Project Type**: Multibranch Pipeline.
- **Branch Sources**: Git (GitHub repository).
- **Script Path**: `07-multibranch-pipeline/Jenkinsfile` (Points to the specific lab folder).
- **Docker Hub**: Versioned tagging using `${BRANCH_NAME}-${BUILD_NUMBER}` (e.g., `feature-login-5`).

---

## Here's What I Actually Did

### Step 1: Refactored the Folder Structure

**Action**: Moved application logic into an `app/` folder while keeping `Dockerfile` and `Jenkinsfile` at the lab root.
**Why**: To separate infrastructure configuration from application code, making the project cleaner and easier to manage.

### Step 2: Configured Multibranch Indexing

**Action**: Created a Multibranch Pipeline project in Jenkins and connected it to my GitHub repo.
**Why**: This eliminates the need to manually create new Jenkins jobs whenever a developer creates a new branch. Jenkins finds them automatically.

### Step 3: Implemented Branch-Specific Logic

**Action**: Used Groovy logic in the `Jenkinsfile` to map specific branches to specific host ports.
**How**: `main` → 5000, `develop` → 5001, `feature-login` → 5002.
**Why**: To prevent "Port already in use" errors when running multiple versions of the app on the same server.

### Step 4: Hardened the Build with .dockerignore

**Action**: Created a `.dockerignore` file to exclude `docs/`, `__pycache__`, and `.git` from the Docker build context.
**Why**: It keeps the Docker image lightweight and prevents local junk files from interfering with the containerized environment.

---

## The "Why" Behind It All

### 1. Why Multibranch Pipeline?

**Think of it like**: An automated librarian who spots a new book on the delivery truck and immediately creates a labeled shelf for it without being asked.
**Key takeaway**: It provides effortless scalability for teams working on multiple features at once.

### 2. Why Dynamic Port Mapping?

**Think of it like**: Assigning different apartment numbers to tenants in the same building. They all live in the same "house" (server), but have their own unique entrance (port).
**Key takeaway**: It enables "Feature Preview" environments where stakeholders can test the `develop` branch without touching the `main` production site.

### 3. Why Branch Name in the Image Tag?

**Think of it like**: Labeling boxes in a warehouse with their department name.
**Key takeaway**: You can look at Docker Hub and instantly know exactly which branch a specific image belongs to without checking Git logs.

---

## Problems I Ran Into And How I Fixed Them

### DNS Resolution Failure

**What happened**: Jenkins failed to scan GitHub with a `Could not resolve host: github.com` error.
**How I fixed it**: Realized it was a temporary network/DNS glitch. I ran `docker restart jenkins-server` to reset the container's network stack, and the scan passed.

### Dockerfile Path Errors

**What happened**: After moving files into the `app/` folder, the Docker build failed because it couldn't find `requirements.txt`.
**How I fixed it**: Updated the `Dockerfile` instructions to `COPY app/requirements.txt .` and adjusted the build context in the `Jenkinsfile`.

---

### Pro Tip

When using Multibranch Pipelines, always use a **`.dockerignore`** file. It is the hallmark of a professional CI/CD pipeline, ensuring your builds are fast, secure, and lean.
