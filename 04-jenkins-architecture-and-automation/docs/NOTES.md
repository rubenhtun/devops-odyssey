# Lesson 04: Jenkins Architecture And Automation

## Shorthand Notes

### Jenkins Home Structure

- Clearly understand what the Jenkins home directory stores: configurations, logs, and plugins.

### Distributed Architecture

- The Jenkins controller acts as the significant brain, while agent nodes perform like motivated hands, managing the build process.

### Parameterized Build

- If someone asks what a dynamic build is, we can confidently answer that branch names, version numbers, and other parameters can be flexibly customized before each build begins.

### Poll SCM

- LOL, it's like a GitHub detective, regularly eager to spy on new changes right on time.

### Environment Variables

- These are dynamic values that automatically change with every single build.

### Workspace

- This is where code is pulled from GitHub, plugins are installed, and logs are executed—all within this temporary working area.

### Execute Shell

- You can test build steps using pre-customized shell scripts.

---

## Detailed Infrastructure Explanation

### 1. The Centralized Controller (The Brain)

The Jenkins Controller is the heart of the infrastructure, running as a Docker container. Its primary responsibilities include:

- **Orchestration:** Deciding when and where a build should start.
- **State Management:** Storing the `Jenkins Home` directory, which contains all plugin data, user credentials, and build logs.
- **Web Interface:** Serving the UI where we configure parameters and monitor the **GitHub Detective** (Poll SCM).

### 2. The Distributed Agents (The Hands)

Instead of running heavy build tasks on the Controller, we use Agent nodes to execute the actual work.

- **Resource Isolation:** This prevents the Controller from crashing if a build consumes too much CPU or memory.
- **The Workspace:** Each Agent maintains a specific `workspace` folder. This is the temporary "workshop" where code is pulled from GitHub and shell scripts are executed.
- **Scalability:** This architecture allows us to add more Agents (Hands) as our project grows, enabling multiple builds to run simultaneously.

### 3. The Automation Pipeline Logic

The "nervous system" that connects the Brain to the Hands consists of:

- **Trigger Mechanism (Poll SCM):** A proactive monitoring system that checks for commits. It ensures the infrastructure reacts to developer changes without human intervention.
- **Environment Injection:** Using **Parameters** like `${BRANCH_NAME}`, Jenkins injects dynamic values into the shell environment at runtime. This turns a static script into a **Dynamic Build**.
- **Verification Loop:** Through the `Execute Shell` step, the infrastructure provides immediate feedback. It validates the directory structure and environment variables, reporting a **Success** or **Failure** status back to the Controller.
