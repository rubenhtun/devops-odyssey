import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    branch = os.getenv('BRANCH_NAME', 'unknown')
    build = os.getenv('BUILD_NUMBER', 'unknown')
    return render_template('index.html', branch_name=branch, build_number=build)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)