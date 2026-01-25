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
        </style>
    </head>
    <body>
        <h1>Welcome to the DevOps Odyssey!</h1>
        <p>This application is running inside a Docker container.</p>
        <hr>
        <p>This lab primarily focuses on the following Jenkins configurations:</p>
        <ul>
            <li>Setting up credentials for Docker Hub.</li>
            <li>Establishing a connection with a source code repository like GitHub.</li>
            <li>Using Git for source code management with secure credentials.</li>
            <li>Configuring environment variables using 'Secret Text' for DOCKER_USERNAME and DOCKER_PASSWORD.</li>
            <li>Automating the build process using sequential execute shell scripts.</li>
        </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

