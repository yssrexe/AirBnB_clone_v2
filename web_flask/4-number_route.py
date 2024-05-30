#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def fs_page():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def sc_page():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_page(text : str):
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text' : 'is cool'} ,strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_page(text : str):
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def num_page(n : str):
        return f"{n} is a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
