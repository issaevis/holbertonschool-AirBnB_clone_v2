#!/usr/bin/python3
'''module for flask with variables and multole routes'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    ttext = text.replace('_', ' ')
    return f"C {ttext}"


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def variable_pyth(text="is cool"):
    ttext = text.replace('_', ' ')
    return f"Python {ttext}"


@app.route('/number/')
@app.route("/number/<n>", strict_slashes=False)
def is_n(n):
    if n == int:
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
