import os
import socket
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    context = {
      'branch_name': os.getenv('BRANCH_NAME', 'N/A'),
      'build_num': os.getenv('BUILD_NUMBER', 'N/A'),
      'hostname': socket.gethostname(),
      'status': 'Healthy'
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)