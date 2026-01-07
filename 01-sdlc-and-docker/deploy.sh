#!/bin/bash

echo "--- Stopping existing container ---"
docker stop devops-odyssey-app || true

echo "--- Removing existing container ---"
docker rm devops-odyssey-app || true

echo "--- Building new image ---"
docker build -t python-app .

echo "--- Starting new container on port 3000 ---"
docker run -d --name devops-odyssey-app -p 3000:5000 python-app

echo "--- Success! App is running at http://localhost:3000 ---"
docker ps | grep devops-odyssey-app