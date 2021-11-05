import sqlite3

connection = sqlite3.connect('flash2brain.db')

cursor = connection.cursor()

cursor.execute("""
INSERT INTO flashcard
	(question, answer, source, creator)
VALUES
	('Wie ist die Antwort auf alle Fragen?', '42', 'https://www.google.com/search?client=firefox-b-d&q=Wie+ist+die+Antwort+auf+alle+Fragen%3F', 'morpheus'),
	('Wird Python mit englischem TH, oder mit Scharfem-S ausgesprochen?', 'Python wird mit englischem TH ausgesprochen.', 'https://dictionary.cambridge.org/de/aussprache/englisch/python', 'anonym'),
	('Oha, ein unsichtbarer Mann schläft in Deinem Bett? Wen rufst Du dann?', 'Ghost Busters!', '', 'morpheus'),
	('In welchem Jahr wurde die Konversionstherapie in Deutschland verboten?', '2020', 'https://www.bundesgesundheitsministerium.de/konversionstherapienverbot.html', 'morpheus'),
	('Was kannst Du Dir unter einer Zugbrücke vorstellen?', 'Wasser', '', 'will nicht genannt werden'),
	('Was ist der Unterschied zwischen einem Nilpferd?', 'Im Wasser schwimmt es, an Land läuft es.', '', 'africa bambaataa');
""")

connection.commit()
connection.close()

