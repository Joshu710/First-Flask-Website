#!/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Remember to stop and smell the flowers!!"

@app.route("/hello")
def hello():
    return "Hello world!"


app.run(host="0.0.0.0", port=80)



