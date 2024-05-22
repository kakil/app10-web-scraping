import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE date='2024.05.24'")
rows = cursor.fetchall()
print(rows)


# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE date='2024.05.24'")
rows = cursor.fetchall()
print(rows)


# Insert new rows
new_rows = [('Bears', 'Bear City', '2024.05.25'),
            ('Tigers', 'Tiger City', '2024.06.24')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()


# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)