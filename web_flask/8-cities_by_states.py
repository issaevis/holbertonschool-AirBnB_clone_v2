#!/usr/bin/python3
'''linking flask with the website!!'''
from flask import Flask
from models import storage
from models.state import State
from models.city import City
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def root_route():
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template("8-cities_by_states.html", states=states, cities=cities)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
