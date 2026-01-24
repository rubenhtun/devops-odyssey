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
        <p>Explore the journey of DevOps and containerization.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)