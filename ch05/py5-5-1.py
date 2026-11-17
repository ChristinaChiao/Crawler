import sqlite3

with sqlite3.connect("smart_scraper.db") as conn:
    cursor = conn.cursor( )
    # 在 url 欄位後面加上 UNIQUE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT UNIQUE,
        price INTEGER
    )
    """)
