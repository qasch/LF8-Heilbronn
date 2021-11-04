#!/usr/bin/env python3
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    connection = sqlite3.connect('db/test.db')
    cursor = connection.cursor()

    # Select Statement ausführen
    # fetchall() sorgt dafür, dass das Ergebnis in einer Liste gespeichert wird
    rows = cursor.execute(""" SELECT * FROM person; """).fetchall()

    # Änderungen übermitteln
    connection.commit()
    # Verbindung zur Datenbank schliessen
    connection.close()

    return render_template('index.html', rows=rows)

@app.route("/grid")
def grid():
    return render_template('grid.html')

if __name__ == '__main__':
    app.run()