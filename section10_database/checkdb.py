import sqlite3

conn = sqlite3.connect('contacts.sqlite')

username = input("Enter a username: ")

# for row in conn.execute('SELECT * FROM sqlite_master'):
for name, phone, email in conn.execute("SELECT * FROM contacts WHERE name = ?", (username,)):
# for name, phone, email in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (username,)): # case insensitive

    print(name, phone, email)

conn.close()


db = sqlite3.connect('accounts.sqlite')
# db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)


for row in db.execute("SELECT * FROM history"):
    print(row)

db.close()

