# Lab Documentation

## Overview

This lab covers advanced Jenkins automation setup, focusing on implementing a CI/CD pipeline using parameters, automation triggers, and Git integration.

## Prerequisites

- Docker and Docker Compose installed (as per Lab 3).
- Git installed with essential branches: `feature-login`, `develop`, and `main`.
- Basic understanding of CI/CD concepts.

---

## 1. Jenkins Home Structure

What is the meaning of home? what's your definition of home? What's are basic criteria to define a home?

Now, let's go back to the topic. Actually, Jenkins also has a home. It's the `/var/jenkins_home` directory. But Jenkins is running inside a Docker container. So, we can understand it can not fully control and manage other things outside its home. However, Jenkins also has its own internal file system to keep everything organized. Think of it like the `/var/jenkins_home` directory as the foundation. On the other hand, folders like `config` and `jobs` are also essential components that maintain the server's settings and keep track of every project's history.

![Jenkins Home Structure](diagrams/jenkins-home-structure.svg)

---

## 2. Automation Workflow

Magic is not only about wizardry or what we see in movies. In tech industry, all about automation can be seen as magic either. Right? That's my POV.

So, what is the magic of automation? The Jenkins automation starts when a developer pushes code to a private or public repository, on GitHub. This action alerts the Jenkins server that something has changed very soon. From there, the Jenkins Controller takes over, guiding its workspace agents to pull the latest code and transform it into a finished product, or artifact without any manual intervention.

![Automation Workflow](diagrams/jenkins-automation-workflow.svg)

---

## 3. Distributed Architecture

We can think of the Distributed Architecture as a "Brain and Hands" setup. The Jenkins Controller performs like a brain—handling part for logic, scheduling, and management of the whole system meanwhile the Agent Nodes act as moveable hands. These agents mainly do the heavy lifting, like running shell scripts, building Docker images, and executing tests. Like an example a boss delegates tasks to his employees. The boss will not do everything by himself, right? If he does, he will get tired and burned out. So, the division of labor ensures that the system stays fast and efficient, even when handling multiple tasks at once.

![Distributed Architecture](diagrams/jenkins-distributed-architecture.svg)

---

## 4. Lab Notes

[View Lab Notes](NOTES.md)

---

## 5. Jenkins Lab Cheatsheet

[View Jenkins Lab Cheatsheet](JENKINS_LAB.md)

---

## 6. How to Setup a New Freestyle Project

### Step 1: Create Freestyle Project

1. Click **New Item** on the Jenkins Dashboard.
2. Enter a project name and select **Freestyle project**.
3. Click **OK** to proceed to the configuration page.

### Step 2: Configure Parameters

1. Check the box **This project is parameterized**.
2. Click **Add Parameter** and select **String Parameter**.

- **Name:** `BRANCH_NAME`
- **Default Value:** `main`
- **Description:** Write anything related to the branch.

### Step 3: Source Code Management (SCM)

1. In the **Git** section, enter **Repository URL**.
2. Under **Branch Specifier**, use the parameter created above: `*/${BRANCH_NAME}`.

### Step 4: Build Triggers

1. Select **Poll SCM**.
2. Enter the schedule `H/2 * * * *` for every 2 minutes to check for code updates automatically.

### Step 5: Build Steps

1. Click **Add build step** and select **Execute shell**.
2. Because we are not using a `Dockerfile` in this lab, we will use this `Execute shell` script for testing purpose.

```bash
echo "--- Starting Build Stage ---"
echo "Building Project for Branch: ${BRANCH_NAME}"
echo "Current Build Number: ${BUILD_NUMBER}"
echo "Workspace Path: ${WORKSPACE}"

# List contents of the project folder
ls -la 04-jenkins-architecture-and-automation/

echo "--- Build Process Completed Successfully ---"
```

---

Finally, we will see this kind of console output.

![Console Output](assets/console-output.png)
