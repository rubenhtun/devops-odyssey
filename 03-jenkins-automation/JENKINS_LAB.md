# Jenkins Automation Lab

### 1. Environment Setup

Jenkins was initialized using Docker, following an **Infrastructure as Code (IaC)** approach.

- **File:** `docker-compose.yml`
- **Key Configurations:**

  - Port `8080` exposed for the Jenkins Dashboard.
  - Volume mount `./jenkins_home` to persist Jenkins data.
  - `/var/run/docker.sock` mapped to allow Jenkins to communicate with the host Docker engine.
  - User set to `root` to avoid basic permission issues during Docker operations.

### 2. Initial Setup Challenges

- **Admin Password:** Retrieved either from the container logs or from the `secrets/initialAdminPassword` file inside the Jenkins home directory.
- **Plugins:** Installed recommended plugins to enable essential CI/CD features, especially Git integration and Pipeline support.

### 3. First Freestyle Job

This exercise verified that Jenkins can successfully execute shell commands.

- **Commands used:** `whoami`, `pwd`, `echo`
- **Learning Outcome:**
  Jenkins creates a dedicated workspace directory for each job under:

  ```
  /var/jenkins_home/workspace/
  ```

  Each job runs in isolation within its own folder.

### 4. GitHub Integration & Docker Build

Real application source code was pulled from GitHub and used to build a Docker image.

- **Repository:**
  `https://github.com/rubenhtun/devops-odyssey.git`

- **Workflow:**

  1. Clone the repository.
  2. Navigate to the `02-git-and-cicd-concepts` directory.
  3. Execute `docker build` to create the image.

### 5. Major Troubleshooting: **"docker: not found"**

- **Issue:**
  The build failed at Step 3 with the error:

  ```
  docker: not found
  ```

- **Root Cause:**
  Although the Jenkins container had access to the host Docker daemon via `docker.sock`, the **Docker CLI was not installed inside the Jenkins container**.

- **Solution:**

  1. Entered the Jenkins container as the root user using `docker exec`.
  2. Installed Docker CLI with:

     ```bash
     apt-get update && apt-get install -y docker.io
     ```

This enabled Jenkins jobs to execute Docker commands successfully.

### 6. Successful Automated Deployment

After resolving the Docker CLI issue, the CI/CD workflow executed successfully end-to-end.

- Jenkins was able to:

  - Pull source code from GitHub.
  - Build a Docker image without errors.
  - Automate the build process through Jenkins jobs.

- This confirmed that:

  - Jenkins can control Docker on the host machine.
  - The CI/CD pipeline environment is correctly configured.

- The setup now supports:

  - Repeatable builds
  - Automated deployments
  - A strong foundation for future pipeline stages such as testing, image pushing, and production deployment.
