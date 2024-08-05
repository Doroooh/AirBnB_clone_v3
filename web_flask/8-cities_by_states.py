#!/usr/bin/python3
""" Initialize Flask web server """

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/state_cities', strict_slashes=False)
def state_cities():
    """Renders an HTML page with states and their cities sorted alphabetically"""
    all_states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=all_states)

@app.teardown_appcontext
def close_storage_session(exception):
    """Close the storage session when the application context is torn down"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
