import sqlite3
conn = sqlite3.connect("userdata.db")

create_table_query = """
create table user_record (name varchar(25),email varchar(50),message varchar(100))
"""

cur = conn.cursor() # temprory memory
cur.execute(create_table_query)
print("Table created !")

cur.close()
conn.close()