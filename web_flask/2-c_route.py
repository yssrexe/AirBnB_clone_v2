#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def fst_page():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def sc_page():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def tr_page(text : str):
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
