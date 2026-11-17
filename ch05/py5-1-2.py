import sqlite3

conn = sqlite3.connect("notes.db") # .dp 或.sqlite

cursor = conn.cursor()

data = (4, "HTML", 1712340000)

sql = "INSERT INTO mytable(_id, note, created) VALUES(?,?,?)"

# sql = "INSERT INTO mytable VALUES(4, 'HTML', 1712340000);"

cursor.execute(sql, data)
conn.commit()
conn.close()
print("資料寫入成功")

