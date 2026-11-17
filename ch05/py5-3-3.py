import sqlite3

# 模擬 BeautifulSoup 抓下來的一組字典
data_from_web = {
    "t": "AI 整合爬蟲新趨勢",
    "d": "2026-04-15",
    "u": "https://school.com/news3"
}

with sqlite3.connect("news_data.db") as conn:
    cursor = conn.cursor( )
    # 使用 :key 的語法來對應字典的 Key
    sql = "INSERT INTO news (title, date, url) VALUES (:t, :d, :u)"
    cursor.execute(sql, data_from_web)
