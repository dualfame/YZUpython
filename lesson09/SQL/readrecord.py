import sqlite3

sql = 'Select * from Lotto'

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
