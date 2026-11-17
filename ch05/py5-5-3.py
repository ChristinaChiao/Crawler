import sqlite3

# 假設這是我們抓到的資料，其中第一筆已經存在資料庫中了
updated_data = ("iPhone 15 降價特賣", "https://news.com/p1", 25000)

with sqlite3.connect("smart_scraper.db") as conn:
    cursor = conn.cursor( )
    # 使用 INSERT OR IGNORE，重複的 URL 會自動被跳過
    cursor.execute("""
    INSERT OR REPLACE INTO articles (title, url, price) 
    VALUES (?, ?, ?)
    """, updated_data)
    
    print(f"執行完畢，影響行數: {conn.total_changes}")
