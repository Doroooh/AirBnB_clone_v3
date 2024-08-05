#!/usr/bin/python3
"""
Sets up a Flask web server
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/all_states', strict_slashes=False)
@app.route('/all_states/<state_id>', strict_slashes=False)
def show_states(state_id=None):
    """Displays states and their cities in alphabetical order, or a specific state if an ID is provided"""
    all_states = storage.all("State")
    if state_id:
        state_id = f'State.{state_id}'
    return render_template('9-states.html', states=all_states, state_id=state_id)

@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage session when the application context ends"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
