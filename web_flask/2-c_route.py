#!/usr/bin/python3
""" Launch the Flask-based web service """

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Shows 'C ' followed by the provided text, with underscores replaced by spaces"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
