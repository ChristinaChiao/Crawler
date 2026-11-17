import sqlite3

# 假設這是我們抓到的資料，其中第一筆已經存在資料庫中了
scraped_data = [
    ("舊聞：iPhone 15 發表", "https://news.com/p1", 29900),
    ("新聞：iPhone 16 預覽", "https://news.com/p2", 32900)
]

with sqlite3.connect("smart_scraper.db") as conn:
    cursor = conn.cursor( )
    # 使用 INSERT OR IGNORE，重複的 URL 會自動被跳過
    cursor.executemany("""
    INSERT OR IGNORE INTO articles (title, url, price) 
    VALUES (?, ?, ?)
    """, scraped_data)
    
    print(f"執行完畢，影響行數: {conn.total_changes}")
