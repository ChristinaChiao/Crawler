import sqlite3

conn = sqlite3.connect("my_scraper.db") # .dp 或.sqlite

cursor = conn.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        link TEXT
    )
'''

cursor.execute(sql)
conn.commit()
conn.close()
print("資料庫與資料表建立成功")

