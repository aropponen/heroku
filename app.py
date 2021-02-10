from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
import os

app = Flask(__name__)

DATABASE_URL = os.environ['postgres://dupswmfsimipmo:40f0b8cba142cd710ec7ba1869d173c3c144779b40afb6dd9cbec578f06c7e17@ec2-54-220-35-19.eu-west-1.compute.amazonaws.com:5432/dbula7ktp10sda']

db = create_engine(DATABASE_URL)

@app.route('/')
def index():
    results = db.execute('SELECT name FROM city')      
    return render_template('cities.html', cities=results)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)