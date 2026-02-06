# Builder Stage
FROM python:3.9-slim AS builder

WORKDIR /app

COPY app/requirements.txt .

# Here, one interesting question is: what is a virtual environment?
# Like the real-life example of having separate rooms in a family for different purposes: a jazz player will play in his jazz jamming room, a bookworm would like to read books in his cozy library room, and you as a developer embrace writing Python spaghetti code in your Python virtual environment workspace.
# Similarly, a Python virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.
# A given specific path allows you to enter and work blissfully without disturbing other projects and their dependencies for sure.
# So, here we are creating a virtual environment in the /app/.venv directory.
RUN python -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Final Stage
FROM python:3.9-slim

# This line installs Node.js in the final image.
# Node.js is required to run the health-check.js script for performing health checks on the Flask application.
RUN apt-get update && apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# This line copies the virtual environment from the builder stage to the final stage.
# But remember that this line filters out all the unnecessary files to keep the final image size lean and efficient.
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD ["node", "static/js/health-check.js"]