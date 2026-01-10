# Lesson 03: Jenkins & Docker Integration

## Shorthand Notes

### 1. Infrastructure

- run Jenkins as a container for CI/CD automation
- map `jenkins_home` volume for data persistence
- use root user to prevent permission denied errors

### 2. Docker-out-of-Docker

- mount `/var/run/docker.sock` to link Jenkins with Host Docker
- Jenkins performs like a "Remote Control" for the host's Docker engine
- install `docker.io` CLI inside Jenkins to send API requests

### 3. Build Workflow

- Jenkins pulls code into a dedicated Workspace
- verify environment using `docker --version` shell command
- trigger Host Docker to build and manage images

---

## Detailed Infrastructure Explanation

### 1. The Controller (Jenkins Container)

- **Technical Breakdown:** Deployed via `docker-compose` with port **8080** and volume mounting.
- **Key Concept:** Provides an isolated environment for automation while keeping data safe on the host.

### 2. Socket Communication (DooD Pattern)

- **Technical Breakdown:** Connecting the host socket bypasses the need for "Docker-in-Docker" (DinD).
- **Key Concept:** Direct communication between the Jenkins container and the Host Docker Daemon.

### 3. API Translation (Docker CLI)

- **Technical Breakdown:** The CLI inside Jenkins converts shell commands into **Docker API calls**.
- **Key Concept:** Essential bridge to avoid `docker: not found` errors during builds.

### 4. Build Validation

- **Technical Breakdown:** Freestyle jobs automate the `git pull` and environment check.
- **Key Concept:** Ensures the workspace is ready and the Docker engine is reachable before building images.
