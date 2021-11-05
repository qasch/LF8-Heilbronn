import sqlite3

# Erstelle die Datenbank test.db
# (falls sie nicht schon vorhanden ist)
connection = sqlite3.connect('flash2brain.db')

cursor = connection.cursor()

# die beiden oberen Zeilen könnten auch
# so geschrieben werden:
#sqlite3.connect('test.db').cursor()

cursor.execute("""
DROP TABLE IF EXISTS flashcard;
""")

cursor.execute("""
CREATE TABLE flashcard (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	question TEXT NOT NULL,
	answer TEXT NOT NULL,
	source TEXT,
	creator TEXT NOT NULL
);

""")

connection.close()

