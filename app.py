from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello heroku!"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)