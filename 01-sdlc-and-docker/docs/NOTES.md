# Lab 01: SDLC & Docker Basics

### 1. SDLC Fundamentals

- Learned the 8 stages: Requirements, Design, Development, Build, Test, Deploy, Operate, and Feedback.
- Understanding the **Software Development Life Cycle** is the foundation for CI/CD automation.

### 2. Programming Languages in DevOps

- **Compiled (Java, Go):** Need to be built into artifacts before running.
- **Interpreted (Python, Node.js):** Run directly via an interpreter but require specific runtime environments.

### 3. Containerization (Docker)

- **Dockerfile:** Used to define the environment, install dependencies, and package the application.
- **Artifacts:** Created a portable Docker Image that contains everything the app needs to run.

### 4. Orchestration & Networking (Docker Compose)

- Used **Docker Compose** to manage multi-container setups.
- Implemented **Virtual Networking** to allow the Web container and Database container (Postgres) to communicate.
- Learned about **Port Mapping** (e.g., `3000:5000`) and **Environment Variables**.
