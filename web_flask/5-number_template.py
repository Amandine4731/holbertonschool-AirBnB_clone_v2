#!/usr/bin/python3
"""
    program to start a flask web application
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    var = f'C {text}'
    return var.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>")
def python_text(text):
    var = f'Python {text}'
    return var.replace("_", " ")


@app.route('/number/<int:n>'; strict_slashes=False)
def n_num(n):
    var = f'{n} is a number'
    return var


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_num_html(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
