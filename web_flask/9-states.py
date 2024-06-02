#!/usr/bin/python3
"""hello route"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception=None):
    """close storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
def ret_States():
    """return states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


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
