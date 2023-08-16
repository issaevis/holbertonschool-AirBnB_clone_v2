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


@app.route("/number/<int:n>", strict_slashes=False)
def is_n(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_n_template(n):
    return render_template("5-number.html", n=n)


if _name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
