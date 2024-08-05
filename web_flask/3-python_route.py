#!/usr/bin/python3
""" Initialize  Flask web server """

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home_page():
    """Return 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Return string 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Shows 'C ' followed by text parameter with underscores replaced with spaces"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_message(text='is cool'):
    """Displays 'Python ' followed by the text parameter with underscores replaced with spaces"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
