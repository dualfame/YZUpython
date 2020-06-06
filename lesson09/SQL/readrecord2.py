import sqlite3
import pandas as pd

sql = 'Select * from Lotto'

conn = sqlite3.connect("demo.db")
df = pd.read_sql_query(sql, con=conn)
print(df.head(10))
conn.close()
