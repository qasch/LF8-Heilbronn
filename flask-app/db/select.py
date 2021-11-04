import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# Select Statement ausführen
# fetchall() sorgt dafür, dass das Ergebnis in einer Liste gespeichert wird
rows = cursor.execute(""" SELECT * FROM person; """).fetchall()

# über alle Datensätze iterieren
# und jeweils in diesem Fall Vorname und Nachname ausgeben
# untereinander ausgeben
for row in rows:
    print(row[1], row[2])

# Änderungen übermitteln
connection.commit()
# Verbindung zur Datenbank schliessen
connection.close()

