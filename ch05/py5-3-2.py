import sqlite3

# 模擬抓到的單筆資料
news_item = ("2026/4/17 午後變天", "2026-04-17", "https://school.com/news2")

# 使用 with 語法，安全又簡潔
with sqlite3.connect("news_data.db") as conn:
    cursor = conn.cursor( )
    cursor.execute("INSERT INTO news (title, date, url) VALUES (?, ?, ?)", news_item)
    # 此處不需要手動 conn.commit( )，with 離開時若無錯誤會自動提交
