# Docker Basic Commands

### 1. Image Management

```bash
# Search for official images on Docker Hub
docker search python

# Download a specific image from Docker Hub to your local machine
docker pull python:3.9-slim

# List all Docker images currently available on your machine
docker images

# Remove a specific image using its ID or Name
docker rmi <image_id_or_name>
```

### 2. Container Lifecycle

```bash
# Create and start a container from an image with port mapping
docker run -d --name my-app -p 3000:5000 python-app

# List only currently running containers
docker ps

# List all containers, including those that are stopped or exited
docker ps -a

# Stop a running container
docker stop <container_id_or_name>

# Start a previously stopped container
docker start <container_id_or_name>

# Remove a stopped container from the system
docker rm <container_id_or_name>
```

### 3. Inspection and Debugging

```bash
# Display the standard output logs of a specific container
docker logs <container_id_or_name>

# Open an interactive terminal inside a running container
docker exec -it <container_id_or_name> /bin/bash

# View detailed information about a container in JSON format
docker inspect <container_id_or_name>
```

### 4. System Maintenance

```bash
# Remove all unused data such as stopped containers, unused networks, and dangling images
docker system prune
```
