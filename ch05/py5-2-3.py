import sqlite3

conn = sqlite3.connect("my_scraper.db") # .dp 或.sqlite

cursor = conn.cursor()

sql="UPDATE products SET price = ? WHERE name = ?"
cursor.execute(sql, (36000.0, "筆記型電腦"))

sql="SELECT * FROM products"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    for i in range(len(row)):
        print(row[i], "|", end='')
    print()

if rows:
    print("資料查詢成功")
    
conn.commit()
conn.close()


