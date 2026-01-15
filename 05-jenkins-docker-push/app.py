from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, DevOps Odyssey!</h1><p>Jenkins successfully built and deployed this app.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)