#!/usr/bin/python3
"""
    program to start a flask web application
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    strict_slashes = False
    var = f'C {text}'
    return var.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def python_text(text):
    strict_slashes = False
    var = f'Python {text}'
    return var.replace("_", " ")


@app.route('/number/<int:n>')
def n_num(n):
    strict_slashes = False
    var = f'{n} is a number'
    return var

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
