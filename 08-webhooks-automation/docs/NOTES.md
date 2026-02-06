# Lab 08: Jenkins Webhooks Automation

In Lab 07, we mastered branch management. In Lab 08, we achieved **True Automation**. Instead of manually clicking "Build Now," we connected GitHub to Jenkins using **Webhooks** and **Ngrok**. This means every time I push code, the pipeline wakes up and deploys itself instantly. We also leveled up our container reliability by adding a **Native Docker Health Check** script and a **Multi-stage Dockerfile** to keep our production images lean and professional.

---

## Quick Cheat Sheet

### Core Ideas

- **Webhooks**: A "push notification" from GitHub to Jenkins to trigger builds immediately upon code changes.
- **Ngrok Tunneling**: Creating a secure public URL for my local Jenkins server so GitHub can "see" it over the internet.
- **Native Health Checks**: A internal script (`health-check.js`) that runs inside the container to monitor if the Flask app is actually responding.
- **Multi-stage Builds**: Using a "Builder" image to compile dependencies and a "Final" slim image to run the app, reducing image size significantly.

### Commands & Configs

```javascript
const options = {
  host: "localhost",
  port: 5000,
  timeout: 2000,
};
```

```dockerfile
# Multi-stage Snippet
FROM python:3.9-slim AS builder
...
FROM python:3.9-slim
RUN apt-get update && apt-get install -y nodejs # Required for health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD node static/js/health-check.js

```

### My Setup

- **Trigger**: GitHub Webhook (Push events).
- **Public Gateway**: Ngrok Tunnel (`http://your-id.ngrok-free.app`).
- **Health Check Language**: Node.js (running inside the Python container).
- **Docker Status**: Displays `(healthy)` in `docker ps` output.

---

## Here's What I Actually Did

### Step 1: Exposed Jenkins to the Internet

**Action**: Ran `ngrok http 8080` and grabbed the public URL.
**Why**: GitHub cannot send webhooks to `localhost`. Ngrok creates a bridge that lets GitHub find my Jenkins server.

### Step 2: Configured the GitHub Webhook

**Action**: Added a webhook in GitHub repository settings using the Ngrok URL + `/github-webhook/`.
**Why**: This tells GitHub: "Hey, every time I push code, send a POST request to this URL so Jenkins knows it's time to work."

### Step 3: Created the Internal Health Check Script

**Action**: Wrote `health-check.js` and placed it in `app/static/js/`.
**Why**: Standard HTTP checks from the outside only tell if the port is open. This internal script verifies if the Python app is actually returning a `200 OK` status.

### Step 4: Refactored to Multi-stage Dockerfile

**Action**: Divided the `Dockerfile` into a `builder` stage for Pip installs and a `final` stage for execution. I also had to install `nodejs` in the final stage.
**Why**: This keeps the final image lightweight (no build tools included) and provides the Node.js runtime needed for the health check script.

---

## The "Why" Behind It All

### 1. Why Webhooks instead of Polling?

**Think of it like**: Getting a text message (Webhook) when a package arrives vs. walking to the front door every 5 minutes to check (Polling). Webhooks are faster and save server resources.

### 2. Why Native Docker Health Checks?

**Think of it like**: An airplane's internal diagnostics. Even if the engines are "running" (Container is Up), the pilot needs to know if the systems are actually working. If the health check fails, Docker can automatically restart the container.

### 3. Why Multi-stage Builds?

**Think of it like**: Using a large kitchen to prep a meal (Builder Stage), but only bringing the finished plate to the dining table (Final Stage). The customer (Production) doesn't need to see the dirty pots and pans (build dependencies).

---

## Problems I Ran Into And How I Fixed Them

### The "Node Module Not Found" Error

**What happened**: The health check was failing with `Error: Cannot find module '/app/health-check.js'`.
**How I fixed it**: I realized my `COPY app/ .` command moved the script to `static/js/health-check.js`. I updated the `HEALTHCHECK` command in the `Dockerfile` to point to the correct path: `CMD node static/js/health-check.js`.

### The Unhealthy Container (Localhost vs. Host)

**What happened**: The container status showed `unhealthy` because I used `host.docker.internal` inside the script.
**How I fixed it**: I learned that since the script runs **inside** the container, it should target `localhost`. Once I changed the host to `localhost`, the status changed to `(healthy)`.

### Missing Node.js in Final Image

**What happened**: The `CMD node` command failed because the Python-slim image doesn't have Node.js installed by default.
**How I fixed it**: Added `RUN apt-get update && apt-get install -y nodejs` to the final stage of the Dockerfile.

---

### Pro Tip

Always check your container health using `docker inspect --format='{{json .State.Health}}' <container_id>`. It gives you the exact error message and exit code from your health check script, making debugging 10x faster!
