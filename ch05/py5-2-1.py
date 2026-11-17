import sqlite3

conn = sqlite3.connect("my_scraper.db") # .dp 或.sqlite

cursor = conn.cursor()

items = [
    ("筆記型電腦", 35000.0, "https://link.com/1"),
    ("無線滑鼠", 899.0, "https://link.com/2"),
    ("機械鍵盤", 2499.0, "https://link.com/3")
]

sql = "INSERT INTO products(name, price, link) VALUES(?,?,?)"
cursor.executemany(sql, items)
print("資料插入成功")

sql="SELECT * FROM products"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(f"name:{row[1]} , price:{row[2]} , link:{row[3]}")

if rows:
    print("資料查詢成功")
    
conn.commit()
conn.close()


