import sqlite3

db = sqlite3.connect('contacts.sqlite')

db.execute('''CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)''')
# Connections execute method does return a cursor
db.execute('''INSERT INTO contacts VALUES ("John", 90111222333, "john@email.com")''')
db.execute('''INSERT INTO contacts VALUES ("Kaan", 90123456, "kaan@email.com")''')

cursor = db.cursor()

cursor.execute('''SELECT * FROM contacts''')
# print(cursor.fetchall()) # [('John', 90111222333, 'john@email.com'), ('Kaan', 90123456, 'kaan@email.com')]
# prints list of tuples all rows one time
# print(cursor.fetchone())  # ('John', 90111222333, 'john@email.com')

for name, phone, email in cursor: # Database cursor is iterable
     # Cursor is kind of generator
    print(name, phone, email)

# cursor.execute('''DROP TABLE contacts''')
cursor.close()
db.commit()
db.close()