# Lab 06: Jenkins Pipeline Automation

## What This Lab Is About

Making sure Jenkins can do all the heavy lifting automatically with a proper **Pipeline as Code**. From cleaning up the workspace to deploying a fresh container—everything happens with one click.

---

## Quick Cheat Sheet

### Core Ideas

- **Pipeline as Code**: The entire CI/CD process exists in a single `Jenkinsfile`.
- **Secret-Keeper Jenkins**: Used Jenkins' built-in credentials store so no passwords live in my code.
- **Smart Tagging**: Every build gets a unique number (`$BUILD_NUMBER`) and the "latest" tag.
- **Clean Deployments**: The pipeline automatically removes old containers so new ones can start fresh.

### Commands I Ran (Inside the Jenkinsfile)

```bash
# Workspace cleanup
cleanWs()

# Grab the latest code from GitHub
checkout scm

# Build with build number and latest tags
docker build -t ${DOCKER_HUB_USERNAME}/${APP_NAME}:${BUILD_NUMBER} .
docker tag ${DOCKER_HUB_USERNAME}/${APP_NAME}:${BUILD_NUMBER} ${DOCKER_HUB_USERNAME}/${APP_NAME}:latest

# Secure login using Jenkins credentials
sh 'echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin'

# Deploy to Port 5000
docker rm -f ${APP_NAME} || true
docker run -d --name ${APP_NAME} -p 5000:5000 ${DOCKER_HUB_USERNAME}/${APP_NAME}:latest
```

### My Setup

- **Pipeline Type**: Declarative Pipeline with a `Jenkinsfile` saved into GitHub.
- **Trigger**: Manual "Build Now" button.
- **Secrets Vault**: Configured `docker-hub-creds` in Jenkins credentials store.
- **Workspace**: Automatic workspace allocation and cleanup for each run.

---

## Here's What I Actually Did

### Step 1: Wrote the Jenkinsfile Blueprint

**Action**: Created a `Jenkinsfile` and defined sequential stages for the Docker workflow.
**Why**: So the build process is version-controlled and repeatable, just like the app code.

### Step 2: Made Jenkins the Password Manager

**Action**: Replaced hardcoded credentials with configured `credentials('docker-hub-creds')`.
**How**: Jenkins injects them as masked environment variables during the run.
**Why**: Security best practice—my Docker Hub password stays encrypted in Jenkins, not in plain text.

### Step 3: Automated the "Build & Tag" Relationship

**Action**: Tagged images with both the Jenkins build number and `latest`.
**Why**: The build number helps me track code history easily—like 'What changed in build #47?'—while the `latest` tag simplifies deployment."

### Step 4: Scripted the Perfect Deployment

**Action**: Wrote steps to force-remove any old container before running the new one.
**Why**: Eliminates manual cleanup and "port already in use" errors. The pipeline handles the lifecycle automatically.

---

## The "Why" Behind It All

### 1. Why `cleanWs()` is the First Step

**Think of it like**: Tidying your desk before starting a new project.
**Key takeaway**: A clean workspace prevents stale files from previous runs from causing build failures.

### 2. Why Jenkins Handles the Secrets

**Think of it like**: Giving a trusted friend your house key instead of hiding it under the mat.
**Key takeaway**: Secure credential management keeps sensitive data out of logs and source control.

### 3. Why We Tag With `latest` AND a Number

**Think of it like**: Naming a photo "Vacation_2025.jpg" but also having it in your "Favorites" album.
**Key takeaway**: You always deploy `:latest` for convenience, but you keep versioned tags for rollbacks.

### 4. Why the Pipeline Removes Old Containers

**Think of it like**: Taking out the trash before bringing in new groceries.
**Key takeaway**: It ensures a predictable, idempotent deployment environment.

---

## Problems I Ran Into And How I Fixed Them

### String Interpolation and Quotes

**What happened**: I used double quotes `""` instead of single quotes `''` in shell commands containing sensitive environment variables, which caused interpretation issues.
**How I fixed it**: I referred to the [official Jenkins String Interpolation documentation](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#string-interpolation), corrected the quoting, and the build passed.

---

### Pro Tip

While we use the "Build Now" button manually in this lab, remember that we can enable **Webhooks** or **Poll SCM** for full automation. That is the ultimate DevOps dream!
