# Lab 02: Git & CI/CD Concepts

## What This Lab Is About

First of all, I consider the "curious coder" phrase would be dominant rather than "happy coder" in the earlier software development industry. In this lab too, my dedication goes on seriously through deep focus to fully understand.

So when building on what I learned before Lab 1 about Docker, I realized something crucial in my mind - actually, packaging our code into related containers is just half of the journey. The real magic happens only when we automate the entire software delivery process. Therefore, I think that's where CI/CD comes in.

One more reminder is that there will be new advanced technologies leading the DevOps industry now. But I guarantee that all former developers are who already knew and used to Git and CI/CD. The reason why is that its underlying technology is pretty cool. Because of them, you are able to collaborate with other developers smoothly, catch bugs joyfully lol, and deliver features reliably.

Overall, my understanding this flow, combined with multiple automated stages, helps me appreciate why DevOps exists and its big impact on software development. Meanwhile, teamwork problems, namely coordinating deployments, preventing broken code from reaching users, and maintaining consistency across environments, are mostly handled by DevOps engineers.

---

## Quick Cheat Sheet

### Core Ideas

- **Git**: Version control system that tracks code changes and allows teams to work on different features without over stepping on each other's jobs.
- **CI/CD**: Continuous Integration for automated testing and building and Continuous Deployment for automated release, also defined as the backbone of modern software delivery.
- **Pipeline**: A series of automated stages that all pushed codes go through from development to production.
- **Artifact**: A finally compiled, tested, and packaged version of our code for sure like a Docker image that's ready for deployment.

---

### Commands I Used

```bash
# Git basics for this lab
git add .
git commit -m "message"
git push origin main
git checkout -b feature/branch-name

# Check repository status
git status
git log --oneline

# Branch management
git branch -a
git merge feature/branch-name
```

---

### My Setup

- **Version Control**: Git with GitHub
- **App**: Flask Python application
- **Container Registry**: Docker Hub for storing images
- **Branching Strategy**: Feature branches → Develop → Main

---

## Here's What I Actually Did

### Stage 1: Understanding Version Control & Branching

**Action**: Explored how Git manages code versions and enables team collaboration.
**How**: Created different branches sucha as feature-login, develop, main and understood the workflow of pushing code and creating pull requests.  
**Why**: Multiple developers need to work on different features simultaneously without breaking the main codebase. So Git branches isolate work to developers and merging is the final step after testing.

### Stage 2: Setting Up the CI/CD Pipeline Foundation

**Action**: Learned the six stages of a complete CI/CD pipeline.  
**How**: Mapped out the flow from Source → Build → Test → Publish → Staging → Production.  
**Why**: Every stage has a purpose. Automating these stages catches issues early and ensures consistent deployments.

### Stage 3: Source Stage (Version Control)

**Action**: Developers push code changes to GitHub using Git commits with intended messages.  
**How**: Code travels from local machine → GitHub repository through branches like feature-login, develop and main.
**Why**: This records all code changes along the way of development. Teams can review back messy or clean code before it's merged to main.
