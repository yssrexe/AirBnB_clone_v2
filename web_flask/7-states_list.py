#!/usr/bin/python3
"""hello_route"""
from flask import Flask, render_template
from models import storage
from models.state import State

# storage.all(...)

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception=None):
    """Closes the storage session"""
    storage.close()


@app.route("/states_list",  strict_slashes=False)
def states_list():
    """shows an html page with a list of states"""

    states = [state for state in storage.all(State).values()]
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
