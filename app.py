from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
import os

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

db = create_engine(DATABASE_URL)

@app.route('/')
def index():
    results = db.execute('SELECT name FROM city')      
    return render_template('cities.html', cities=results)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)