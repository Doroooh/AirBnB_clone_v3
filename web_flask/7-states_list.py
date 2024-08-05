#!/usr/bin/python3
""" Launch Flask web server """

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/list_states', strict_slashes=False)
def list_states():
    """Displays an HTML page with states sorted alphabetically"""
    all_states = list(storage.all("State").values())
    sorted_states = sorted(all_states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage session upon teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
