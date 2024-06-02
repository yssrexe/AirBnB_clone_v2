#!/usr/bin/python3
"""hello_route"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception=None):
    """Closes the storage session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """fetches all states and presents them on html page"""
    allstates = storage.all(State).values()
    return render_template("9-states.html", states=allstates)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """fetches a state by id and its cities and presents them on html page"""
    state = None
    try:
        state = storage.all(State)[f'State.{id}']
    except KeyError:
        pass
    return render_template("9-states.html", state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)