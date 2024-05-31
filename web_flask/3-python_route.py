#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def fst_page():
    """This route returns a "Hello HBNB!" string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def sc_page():
    """This route returns a "HBNB!" string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def tr_page(text: str):
    """This route returns a "c is fin" string"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_page(text: str):
    """This route returns a "python is cool" string"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
