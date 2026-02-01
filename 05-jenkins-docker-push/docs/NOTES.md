# Lab 05: Jenkins Docker Push Pipeline

## What This Lab Is About

Learning how to set up a Jenkins pipeline that builds Docker images and pushes them to Docker Hub. I manually triggered builds to understand each stage step-by-step.

---

## Quick Cheat Sheet

### Core Ideas

- **Pipeline as Script**: Write the whole CI/CD process using shell commands.
- **Tag Smart**: Use build numbers for tracking + "latest" for easy deployment.
- **Keep Secrets Secret**: Use `--password-stdin` so passwords don't end up in logs.
- **Clean Up**: Kill old containers before starting new ones.

### Commands I Used

```bash
# Lab folder
cd 05-jenkins-docker-push

# Build and tag
docker build -t <DOCKER_HUB_USERNAME>/<APP_NAME>:${BUILD_NUMBER} .
docker tag <DOCKER_HUB_USERNAME>/<APP_NAME>:${BUILD_NUMBER} <DOCKER_HUB_USERNAME>/<APP_NAME>:latest

# Login without exposing password
echo $PASSWORD | docker login --username $USERNAME --password-stdin

# Push both versions
docker push <DOCKER_HUB_USERNAME>/<APP_NAME>:${BUILD_NUMBER}
docker push <DOCKER_HUB_USERNAME>/<APP_NAME>:latest

# Clean up first before deploy
docker rm -f <CONTAINER_NAME> || true
docker run -d --name <CONTAINER_NAME> -p 5000:5000 <DOCKER_HUB_USERNAME>/<APP_NAME>:latest
```

### My Setup

- **Code Source**: GitHub repo, main branch
- **Build Trigger**: Manually triggered using "Build Now" in Jenkins
- **Registry**: Docker Hub
- **Secrets**: Jenkins credential store, safer than hardcoding
- **Port Setup**: Turned off Mac's AirPlay to free port 5000, then mapped host:5000 → container:5000

- **Note**: Focused on manual builds to understand the pipeline mechanics without webhooks or polling SCM. In production, I can add webhooks for automatic triggering.

---

## Here's What I Actually Did

### Step 1: Set Up Basic Jenkins Project

**Action**: Created a Jenkins pipeline project.  
**How**: Configured GitHub repo manually, used "Build Now" for triggering.  
**Why**: Wanted to control and observe each build step manually first.

### Step 2: Build the Pipeline Stages

**Action**: Set up build → test → push → deploy steps.  
**How**: Each stage runs in a clean Jenkins workspace.
**Why**: If something breaks early, it stops fast similarly in fail-fast principle.

### Step 3: Handle Passwords Safely

**Action**: Put Docker Hub credentials in Jenkins, used stdin to pass them.  
**How**: Jenkins stores them encrypted, passes as env vars during build.  
**Why**: So my passwords don't show up in build logs.

### Step 4: Tag Images Right

**Action**: Tagged with both build number AND "latest".  
**How**: `${BUILD_NUMBER}` for version tracking, "latest" for easy reference.  
**Why**: If something breaks, I can roll back to a previous build number.

### Step 5: Deploy Cleanly

**Action**: Removed old container, started new one.  
**How**: `docker rm -f` to force remove, then `docker run` with port mapping.  
**Why**: Avoids "port already in use" errors and keeps things tidy.

---

## The "Why" Behind It All

### 1. Why Pipeline Stages Matter

**Think of it like**: An assembly line where each station checks quality before passing to the next.  
**Key takeaway**: Catch bugs early before they reach users.

### 2. Why Image Tagging Strategy Matters

**Think of it like**: Version control for your containers.  
**Key takeaway**: Containers should be immutable—never edit a running one, just deploy a new version.

### 3. Why Credential Security Matters

**Think of it like**: Never writing your password on a sticky note.  
**Key takeaway**: `--password-stdin` keeps passwords out of logs and command history.

### 4. Why Container Cleanup Matters

**Think of it like**: Clearing the table before serving new food.  
**Key takeaway**: Stateless containers = disposable containers.

---

## Problems I Ran Into And How I Fixed Them

### "Port 5000 already in use" on Mac

**Why**: MacOS AirPlay Receiver claims port 5000 by default.  
**Fix**: Turned AirPlay off, then mapped host port 5000 to container port 5000.

### Docker push authentication fails

**Why**: Credentials not set up right.  
**Fix**: Double-check Jenkins credential ID matches what's in the pipeline.

### Old container won't die

**Why**: Sometimes containers get stuck.  
**Fix**: `docker rm -f` forces removal, or `docker kill` then `docker rm`.

---

### Pro Tip

Always tag with build numbers in production—relying only on "latest" can get messy if you need to roll back.
