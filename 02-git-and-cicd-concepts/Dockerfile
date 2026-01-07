# 1. Define the Runtime Environment
FROM python:3.9-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the Dependencies list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code to the container
COPY app.py .

# 5. Define the command to run the application
CMD ["python", "app.py"]
