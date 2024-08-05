#!/usr/bin/python3
""" Launch Flask-based web service """

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """Return 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Return 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """Displays 'C ' followed by the text with underscores replaced by spaces"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_message(text='is cool'):
    """Displays 'Python ' followed by the provided text or defaults to 'is cool'"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:num>', strict_slashes=False)
def number_check(num):
    """Displays 'num is a number' only if num is an integer"""
    return f"{num} is a number"

@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num):
    """Renders an HTML page if num is an integer"""
    return render_template('5-number.html', num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
