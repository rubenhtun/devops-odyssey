import os
from flask import Flask

app = Flask(__name__)

ENV_TYPE = os.getenv('ENV_TYPE', 'Development')
APP_VERSION = "v1.0"
DB_HOST = os.getenv('DB_HOST', 'Not Connected')
APP_COLOR = os.getenv('APP_COLOR', 'lightblue')

@app.route('/')
def home():
    return f"""
    <html>
        <body style="background-color:{APP_COLOR}; font-family: sans-serif; padding: 50px;">
            <h1>Welcome to DevOps Odyssey - Lab 02</h1>
            <p>This application is running inside a Docker container.</p>
            <hr>
            <p><b>Environment:</b> {ENV_TYPE}</p>
            <p><b>Status:</b> Deployment Successful!</p>
            <p><b>Version:</b> {APP_VERSION}</p>
            <p><b>Connected Host:</b> {DB_HOST}</p>
            <hr>
            <p>This lab primarily focuses on Git and CI/CD concepts:</p>
            <ul>
                <li>Understanding Git version control</li>
                <li>Introduction to CI/CD concepts</li>
                <li>Setting up CI/CD pipelines</li>
                <li>Automating deployments with Docker and Docker Compose</li>
            </ul>
            <hr>
            <p><strong>Source Code:</strong> <a href="https://github.com/rubenhtun/devops-odyssey/tree/main/02-git-and-cicd-concepts" target="_blank">View on GitHub</a></p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)