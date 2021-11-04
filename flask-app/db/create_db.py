import sqlite3

# Erstelle die Datenbank test.db
# (falls sie nicht schon vorhanden ist)
connection = sqlite3.connect('test.db')

cursor = connection.cursor()

# die beiden oberen Zeilen könnten auch
# so geschrieben werden:
#sqlite3.connect('test.db').cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS person
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                vorname TEXT, 
                nachname TEXT);
""")

connection.close()

