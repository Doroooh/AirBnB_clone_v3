#!/usr/bin/python3
""" Set up Flask web server """

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """Respond with 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Respond with 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Shows 'C ' followed by the provided text with underscores replaced by spaces"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Display 'Python ' followed by provided text, defaulting to 'is cool'"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:num>', strict_slashes=False)
def number_display(num):
    """Displays 'num is a number' only if num is an integer"""
    return f"{num} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
