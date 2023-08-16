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
    for letter in text:
        if letter is "_":
            letter = " "

    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
