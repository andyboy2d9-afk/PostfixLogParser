import sqlite3


connection = sqlite3.connect('postfixlogparser.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS login (
date TEXT,
ip TEXT,
username TEXT,
proto TEXT
)
''')


connection.commit()

connection.close()