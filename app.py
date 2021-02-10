from flask import Flask
from flask import render_template, jsonify
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


def get_db_data():
    DATABASE_URL = os.environ['DATABASE_URL']
    db = create_engine(DATABASE_URL)

    sql = text('SELECT * from alcohol_license_places')
    results = db.execute(sql)
    return results

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/all')
def api():
    results = get_db_data()

    data = []
    line = 0 

    for row in results:
        r = [row['name'],row['address'], row['postcode'],  row['city'],  row['license_granting_date'],  row['license_type'], row['business_id']]
        data.insert(line, r)
        line +=1

    return jsonify({'data': data})

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)