from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Odyssey</title>
        <style>
            body {
                background-color: lightblue;
                font-family: sans-serif;
                padding: 50px;
            }
            h1 { color: #333; }
            hr { margin: 20px 0; }
            a { color: #0066cc; }
        </style>
    </head>
    <body>
        <h1>Welcome to DevOps Odyssey - Lab 06</h1>
        <p>This Jenkins Pipeline application is running inside a Docker container.</p>
        <hr>
        <p><strong>Lab 06: Jenkins Pipeline</strong> focuses on the following automation steps:</p>
        <ul>
            <li>Pulled source code from GitHub</li>
            <li>Created Docker image with build number tagging</li>
            <li>Uploaded image to Docker Hub registry</li>
            <li>Automatic container replacement on Port 5000</li>
            <li>Workspace sanitized for the next run</li>
        </ul>
        <hr>
        <p><strong>Source Code:</strong> <a href="https://github.com/rubenhtun/devops-odyssey/tree/main/06-jenkins-pipeline" target="_blank">View on GitHub</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)