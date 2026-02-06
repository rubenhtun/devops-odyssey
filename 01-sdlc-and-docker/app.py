from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <body style="background-color: lightblue; font-family: sans-serif; padding: 50px;">
            <h1>Welcome to DevOps Odyssey - Lab 01</h1>
            <p>This application is running inside a Docker container.</p>
            <hr>
            <p>This lab primarily focuses on software development lifecycle (SDLC) and containerization:</p>
            <ul>
                <li>Understanding the SDLC process</li>
                <li>Introduction to Docker and containerization</li>
                <li>Building and running Docker containers</li>
                <li>Best practices for containerized applications</li>
            </ul>
            <hr>
            <p><strong>Source Code:</strong> <a href="https://github.com/rubenhtun/devops-odyssey/tree/main/01-sdlc-and-docker" target="_blank">View on GitHub</a></p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)