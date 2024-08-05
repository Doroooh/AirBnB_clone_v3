#!/usr/bin/python3
""" Initialize the Flask web service """

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/filters_page', strict_slashes=False)
def show_filters():
    """Render an HTML page similar to 6-index.html from static"""
    state_objects = storage.all("State").values()
    amenity_objects = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=state_objects,
                           amenities=amenity_objects)

@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage connection when tearing down"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
