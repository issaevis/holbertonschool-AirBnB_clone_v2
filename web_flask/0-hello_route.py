#!/usr/bin/python3


from flask import Flask
'''module for the first flask program'''
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "<p>Hello HBNB!</p>"
