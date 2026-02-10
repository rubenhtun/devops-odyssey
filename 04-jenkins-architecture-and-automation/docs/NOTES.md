# Lab 04: Jenkins Architecture And Automation

## What This Lab Is About

A bit of extending our curiosity about Jenkins architecture and automation. Nothing is unreasonable; most everything has its own behind-the-scenes reason if we dig deep enough. In this lab, we will be exposed to some parts of Jenkins' home. That's it. By the way, the Docker compose file for this lab either is still the same as before.

---

## Quick Cheat Sheet

### Core Ideas

- **Jenkins Controller**: The brain of the operation—handles scheduling, orchestration, and serves the web UI.
- **Agent Nodes**: The hands that execute actual build tasks. They maintain isolated workspaces and can scale horizontally.
- **Jenkins Home (`/var/jenkins_home`)**: The central storage location containing configurations, job histories, plugins, and workspace data.
- **Parameterized Build**: A dynamic build system where variables like branch names or version numbers are injected before execution.
- **Poll SCM**: An automated trigger mechanism that periodically checks GitHub for new commits and automatically starts builds.
- **Environment Variables**: Built-in dynamic values like `${BUILD_NUMBER}`, `${WORKSPACE}`, and `${BRANCH_NAME}` that change with every build.
- **Workspace**: A temporary directory where Jenkins clones code and executes build commands. And gets cleaned up after builds to save space.

---

### Commands I Used

```bash
# Start Jenkins container
docker-compose up -d

# Check running containers
docker ps

# Access Jenkins container as root
docker exec -it jenkins-server bash

# Navigate to Jenkins home directory
cd /var/jenkins_home

# List Jenkins home structure
ls -la /var/jenkins_home

# View specific job configuration
cat /var/jenkins_home/jobs/<JOB_NAME>/config.xml

# Check workspace contents
ls -la /var/jenkins_home/workspace/<JOB_NAME>

# Manual workspace cleanup in case of need
rm -rf /var/jenkins_home/workspace/<JOB_NAME>/*
```

---

### My Setup

- **Architecture**: Jenkins Controller running in Docker with distributed agent capability
- **Automation Trigger**: Poll SCM checking GitHub every 2 minutes (`H/2 * * * *`)
- **Parameters**: `BRANCH_NAME` parameter for dynamic branch selection
- **Git Integration**: Branch specifier using `*/${BRANCH_NAME}` for flexible builds
- **Build Tool**: Freestyle job with Execute Shell scripts
- **Persistence**: `jenkins_home` volume for configuration and job history

---

- Architecture: Jenkins Controller running in Docker with distributed agent capability
- Automation Trigger: Poll SCM checking GitHub every 2 minutes (H/2 * * * *)
- Parameters: BRANCH_NAME parameter for dynamic branch selection
- Git Integration: Branch specifier using */${BRANCH_NAME} for flexible builds
- Build Tool: Freestyle job with Execute Shell scripts
- Persistence: jenkins_home volume for configuration and job history

---

## Here's What I Actually Did

### Stage 1: Exploring Jenkins Home Structure

Action: Investigated the internal file system of Jenkins to understand where everything is stored.
How: Accessed the Jenkins container and navigated through /var/jenkins_home, examining folders like config.xml, jobs/, plugins/, and workspace/.
Why: Sometimes breaking and taking apart something to detect what inner it is cool, isn't it? If almost everything is covered by abstraction layers, it may lead to stupidity. So, understanding the file structure is crucial because it reveals how Jenkins organizes data.

### Stage 2: Understanding Distributed Architecture

Action: Learned the "Brain and Hands" model of Jenkins infrastructure.
How: Studied how the Jenkins controller, brain orchestrates builds while agent nodes, hands execute the actual work.
Why: Here, my opinion is that managing a big job with separate delegations is a smarter way than being a solo workaholic. Dividing delegations is brilliant for scalability and resource management, right? If only the controller had to run every build itself, it would quickly become overwhelmed and crash. By delegating heavy tasks to multiple agents, the controller will become calm, responsive, and can manage multiple concurrent builds. On the other hand, each agent will maintain its own isolated workspace, preventing build conflicts. This architecture also allows horizontal scaling, just add more agent nodes as my project grows. 

### Stage 3: Setting Up Parameterized Builds

Action: Created a dynamic build system using parameters instead of hardcoded values.
How: Configured a BRANCH_NAME parameter in the Freestyle job, then used */${BRANCH_NAME} as the Git branch specifier.
Why: Without parameters, I'd need separate jobs for main, develop, and feature branches—that's messy and hard to maintain. With parameterization, one job handles all branches. I can trigger a build and specify which branch to use on-the-fly. This is the difference between static configuration and dynamic automation. The ${BRANCH_NAME} variable gets injected into the shell environment at runtime, making scripts adaptable.

### Stage 4: Implementing Automated Triggers with Poll SCM

Action: Set up Jenkins to automatically detect code changes and trigger builds without manual intervention.
How: Enabled Poll SCM with the schedule H/2 * * * *, which checks my GitHub repo every 2 minutes for new commits.
Why: As a lazy man, I often seek an alternative, convenient way. I love this quote: "People with no life, trying to automate their life." Thus, this is where real automation begins!!! Poll SCM acts like a GitHub detective that constantly monitors the repository for changes. When something changes on the repo, it automatically triggers a build. True CI/CD means code flows automatically from commit to deployment.

### Stage 5: Working with Environment Variables

Action: Use Jenkins' built-in environment variables to make build scripts dynamic and informative.
How: Used variables like ${BUILD_NUMBER}, ${WORKSPACE}, and ${BRANCH_NAME} in Execute Shell scripts to display some build context.
Why: Easy to trace where and what bad scenario has happened. So, these environment variables help me debuggable through reading each scenario.

### Stage 6: Understanding Workspace Cleanup Strategy

Action: Learned when and how to clean up workspace directories after builds. How: Explored the workspace folder structure and understood that code accumulates after each build and became much messy.
Why: Almost everything on earth has trade off, haha. The same applies to workspaces, which can consume significant disk space over time, especially with frequent builds. So, cleanup is a part of duty. But one thing I keep in mind is that I have to push artifacts to a safe registry first before cleaning the workspace. If not, I'll lose my build outputs.

---

Pro tip: H/2 * * * * is so intensive because I'm afraid to get banned from GitHub, haha. So, I suggest using H/5 * * * * instead
