import os
from flask import Flask

app = Flask(__name__)

ENV_TYPE = os.getenv('ENV_TYPE', 'Development')
APP_VERSION = "v1.0"
DB_HOST = os.getenv('DB_HOST', 'Not Connected')
APP_COLOR = os.getenv('APP_COLOR', 'white')

@app.route('/')
def home():
    return f"""
    <html>
        <body style="background-color:{APP_COLOR}; font-family: sans-serif; padding: 50px;">
            <h1>DevOps Odyssey - {ENV_TYPE} Environment</h1>
            <p><b>Status:</b> Deployment Successful!</p>
            <p><b>Version:</b> {APP_VERSION}</p>
            <p><b>Connected Host:</b> {DB_HOST}</p>
            <hr>
            <p>This application demonstrates the <b>'Build Once, Run Anywhere'</b> principle of CI/CD.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)