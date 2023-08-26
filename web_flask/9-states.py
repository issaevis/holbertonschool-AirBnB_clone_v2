#!/usr/bin/python3
'''linking flask with the website!!'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, mode="all")


@app.route('/states/<id>', strict_slashes=False)
def show_state_cities(id):
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template("9-state.html", state=state, mode="id")
        return render_template("9-state.html", state=state, mode="none")


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
