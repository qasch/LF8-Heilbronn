import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO person ( vorname, nachname )
        VALUES  ("Peter", "Lustig" ), 
                ("Karl", "Valentin"), 
                ("Heinz", "Erhard");
""")

connection.commit()
connection.close()

