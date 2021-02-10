from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']

db = create_engine(DATABASE_URL)

@app.route('/')
def index():
    return 'Stop it Flask!'


if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)