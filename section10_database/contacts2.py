import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = "update@update.com"
filter_phone = input("Enter a phone number to update: ")

# update_sql = "UPDATE contacts SET email = '{0}' WHERE contacts.phone = {1}".format(new_email, filter_phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?" # This way much safer for SQL injection
                                                                        # and don't allow extra sql statements , sanitizes values
print(update_sql)
update_cursor = db.cursor()
# update_cursor.execute(update_sql)
update_cursor.execute(update_sql, (new_email, filter_phone)) # We must use as tuple for parameters list
# Python quite clever, don't allow multiple statements to be used
# when we call the execute method

# update_cursor.executescript(update_sql)
# executescript method is designed for more than one sql statement in a single call
# individual statements should be separated by semicolon
# Its open to SQL Injection attack like input - "1234; drop table contacts"

print("{} rows updated".format(update_cursor.rowcount))

update_cursor.close()

for name, phone, email in db.execute('SELECT * FROM contacts'):
    print(name, phone, email)
    print("*" * 28)

db.commit()
db.close()