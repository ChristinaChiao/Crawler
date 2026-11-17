import sqlite3

conn = sqlite3.connect("notes.db") # .dp 或.sqlite

cursor = conn.cursor()

sql = "SELECT * FROM mytable"

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(f"_id:{row[0]} , note:{row[1]} , created:{row[2]}")

conn.commit()
conn.close()
print("資料讀取成功")

