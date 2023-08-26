#!/usr/bin/python3
'''linking flask with the website!!'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def root_route():
    cities_by_state = {}
    states = storage.all("State").values()
    for state in states:
        cities_by_state[state.name] = state.cities
    return render_template("8-cities_by_states.html", states=states, cities=cities_by_state)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
