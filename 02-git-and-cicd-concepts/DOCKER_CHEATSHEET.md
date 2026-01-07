# Docker & CI/CD Practical Commands

### 1. Building the Artifact

```bash
# Build a Docker image with a specific name and version tag
docker build -t rubenhtun/devops-odyssey:v1.0 .
```

### 2. Publishing to Registry

```bash
# Authenticate your terminal with Docker Hub
docker login

# Upload the local image to the remote Docker Hub repository
docker push rubenhtun/devops-odyssey:v1.0
```

### 3. Running the Application (Deployment)

```bash
# Start all services defined in docker-compose.yml in detached mode
docker-compose up -d

# Restart services to apply configuration changes (Down then Up)
docker-compose down && docker-compose up -d

# View and follow real-time logs from running containers
docker-compose logs -f
```

### 4. Cleanup & Maintenance

```bash
# Remove all stopped containers to free up resources
docker container prune

# Remove all unused images, including those not used by any container
docker image prune -a
```
