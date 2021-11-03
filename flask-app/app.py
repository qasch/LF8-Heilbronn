#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return "<h1>Hallo Flask :)</h1>"

@app.route("/huhu")
def huhu():
    return "Huhu Du"

@app.route("/grid")
def grid():
    return render_template('grid.html')
