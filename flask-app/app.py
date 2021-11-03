#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return "<h1>Hallo Flask :)</h1>"

@app.route("/huhu")
def huhu():
    return "<h1>Huhu Du.</h1>"
