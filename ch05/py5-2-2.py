import sqlite3

conn = sqlite3.connect("my_scraper.db") # .dp 或.sqlite

cursor = conn.cursor()

sql="SELECT name, price FROM products WHERE price > ? ORDER BY price DESC"
cursor.execute(sql, (1000,))
rows = cursor.fetchall()

for row in rows:
    print(f"name:{row[0]} , price:{row[1]}")

if rows:
    print("資料查詢成功")
    
conn.commit()
conn.close()


