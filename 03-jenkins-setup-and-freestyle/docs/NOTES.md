# Lab 03: Jenkins & Docker Integration

## What This Lab Is About

So I have come across Labs 1 and 2 successfully and actively far. Now it's time to jump into another critical turning point. Both Labs 1 and 2 taught me to an extent about containerizing apps and understanding the CI/CD pipeline concept simply. My dogged mindset is feeling never enough at any sort of learning journey, thirsty for new implementation challenges above all theories which make me vague and unclear.

Along with me, the question is how to automate the entire CI/CD process? Not just theoretically understand it, but how to really happen based on Jenkins, a system where code changes automatically trigger builds, tests, and deployments without me clicking buttons manually?

If someone asked me how I understand Jenkins, I would confidently say "Of course!". And my deep response would be Jenkins is like a door guard serving to protect the house's safety. Whenever someone wants to enter the house, the door guard checks them first. If the person is untrustworthy, he stops them immediately. Only trusted people are allowed to enter.

In real systems, Jenkins also does the same thing. It checks the code by building and testing it before allowing it to go to production. But remember that when Jenkins needs to run Docker commands, it has Docker CLI but not its own Docker Engine. So it cannot build something else, like Docker Images inside itself. Instead, it borrows the boss’s Docker Engine, which already exists in the house via socket mounting.

So, I think this is defined as Docker-out-of-Docker, because Jenkins uses the host’s Docker rather than running a new Docker engine inside itself.

---

## Quick Cheat Sheet

### Core Ideas

- **Jenkins**: An automation server that works for scheduled jobs planned across the entire CI/CD pipeline on time.
- **Docker-out-of-Docker (DooD)**: A well-drawn relationship between local host's Docker daemon of specific Jenkins container, no more new building of Docker inside Jenkins itself.
- **Socket Mount**: The `/var/run/docker.sock` file is a medium communicator to bridge between containers and Docker daemon locating in the host.
- **Freestyle Job**: A traditional Jenkins job in which shell commands and some configurations can be managed ahead. And it will sequentially run passing green mark testing stages.
- **Build Workspace**: An isolated directory in any local folder where Jenkins clones all code and executes build commands.

---

### Commands I Used

```bash
# Start the Jenkins container
docker-compose up -d

# Check Jenkins logs for initial admin password
docker logs jenkins-server

# Access the initial admin password directly
docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword

# Login to Jenkins container as root to install Docker CLI
docker exec -it -u root jenkins-server bash

# Inside Jenkins container, install Docker CLI
apt-get update && apt-get install -y docker.io

# Verify Docker CLI is working
docker --version
```

---

### My Setup

- **Automation Server**: Like above I said, Jenkins running in Docker engine
- **Container Orchestration**: Managing many containers systematically and automatically
- **Persistence**: `jenkins_home` volume used for job configurations and save data consistently
- **Access**: Port 8080 for Jenkins web dashboard interface
- **Build Tool**: Freestyle jobs for initial automation

---

## Here's What I Actually Did

### Stage 1: Understanding the First Problem

**Action**: Tried to realize how Jenkins in a container builds other Docker containers without having its own Docker Engine.
**How**: Brainstorming question here is: if the heavy Docker Engine gets already stuck inside every Jenkins container, how can Jenkins, itself a Docker container easily build upcoming containers? Obviously, the next coming containers will also need Docker Engine. So it sounds like "Docker-in-Docker". The side effect is complexity and heavy resource usage.
**Why**: Something popped up in my brain as an elegant solution. No need to run Docker inside Jenkins anymore. Instead, let Jenkins communicate directly with the host's Docker daemon. And build any kind of new container.

### Stage 2: Setting Up Jenkins Infrastructure

**Action**: Deployed Jenkins as a container with proper configurations
**How**: Used `docker-compose.yml` to define:

- Port mapping 8080 for web dashboard access
- Volume mounting `jenkins_home` for persistent data
- Socket mounting `/var/run/docker.sock` for Docker access
- Privileged `true` mode and root user to avoid permission issues
  **Why**: Because each type of configuration solves a specific problem. Volumes can keep data safe enough anytime pipeline restarts. Socket mounting is main key to letting Jenkins control over Docker to build new containers. Final, about privileged mode is to removes security barriers during manual setup.

### Stage 3: Initial Jenkins Configuration

**Action**: Unlocked Jenkins and installed essential plugins
**How**:

- Accessed Jenkins dashboard at `http://localhost:8080`
- Retrieved initial admin password from container or logs
- Installed suggested plugins plus Git and Pipeline plugins
- Created a basic admin account
  **Why**: Defaults are not too good. To be better, plugins extend their capabilities further. Git plugin comes to play and interacts with my GitHub repositories. Pipeline plugins are crucial for advanced automation later.

### Stage 4: Installing Docker CLI Inside Jenkins

**Action**: Added Docker command-line tools inside the Jenkins container.
**How**: Executed `apt-get install -y docker.io` inside the Jenkins container.
**Why**: Actually, the Jenkins container has the socket mounted, but it doesn't have the Docker CLI tools to talk through that socket in reverse. Without Docker CLI, Jenkins can't send commands to the host's Docker engine. Installing it bridges that gap.

### Stage 5: Creating Your First Freestyle Job

**Action**: Built a simple automation job that verifies the Docker environment.
**How**: Created a Freestyle job that:

- Clones code from a Git repository
- Runs `docker --version` to verify Docker access
- Executes basic shell scripts
  **Why**: I need to overlap theory with real practice. So, the freestyle job proves that Jenkins successfully reached the host's Docker daemon and executed commands I put.

---

## My "LOL-JOY" Moment

Honestly say that Docker-out-of-Docker (DooD) pattern seemed confusing at first. Step by step understanding it, my view became clear about it. For example, the `/var/run/docker.sock` can be metaphorically imagined as a two-way telephone line between the Jenkins container and the host's Docker daemon to communicate with each other. By mounting this socket only, Jenkins gains the ability to:

- Check Docker status
- Build Docker images
- Push images to registries
- Run containers on the host

It's not that Jenkins is running and managing Docker internally. Jenkins has just reliable permission to talk to the host's Docker engine serving as a local tool. This way becomes much simpler than traditional Docker-in-Docker solutions.

**Pro tip:** Make sure Docker CLI is properly installed inside Jenkins before running your first build. The error `docker: not found` means you skipped the CLI installation step, which is easy and unnoticeable to overlook!
