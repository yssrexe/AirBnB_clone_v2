#!/usr/bin/python3
"""number_template"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def fs_page():
    """This route returns a "Hello HBNB!" string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def sc_page():
    """This route returns a "HBNB!" string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_page(text: str):
    """This route returns a "c is fin" string"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_page(text: str):
    """This route returns a "python is cool" string"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num_page(n: str):
    """This route returns a "number" string"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_num(n):
    """This route returns a "number" string"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
