#!/usr/bin/env python3
from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    connection = sqlite3.connect('db/flash2brain.db')
    cursor = connection.cursor()

    # Select Statement ausführen
    # fetchall() sorgt dafür, dass das Ergebnis in einer Liste gespeichert wird
    rows = cursor.execute(""" SELECT * FROM flashcard; """).fetchall()

    # Änderungen übermitteln
    connection.commit()
    # Verbindung zur Datenbank schliessen
    connection.close()

    return render_template('index.html', rows=rows)

@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        # Logik, um Formulardaten in Datenbank einzufügen
        question = request.form['question']
        answer = request.form['answer']
        source = request.form['source']
        creator = request.form['creator']

        connection = sqlite3.connect('db/flash2brain.db')
        cursor = connection.cursor()

        # SQL Insert
        # cursor.execute(f""" INSERT INTO flashcard
        #                     ( question, answer, source, creator )
        #                     VALUES
        #                     (  {question}, {answer}, {source}, {creator} )
        #                     """
        #                )
        cursor.execute(""" INSERT INTO flashcard 
                             ( question, answer, source, creator ) 
                             VALUES 
                             ( ?, ?, ?, ? )
                             """, (question, answer, source, creator)
                       )

        # Änderungen übermitteln
        connection.commit()
        # Verbindung zur Datenbank schliessen
        connection.close()
        return redirect(url_for('index'))
    else:
        return render_template('insert.html')

@app.route("/update")
def update():
    return render_template('update.html')


if __name__ == '__main__':
    app.run()