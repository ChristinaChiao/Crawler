import sqlite3
def init_db( ):
    """初始化資料庫並建立表格"""
    with sqlite3.connect("news_data.db") as conn:
        cursor = conn.cursor( )
        # 建立新聞資料表
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            date TEXT,
            url TEXT UNIQUE
        )""")
        # 日期時間 TEXT INTEGER
        # conn.commit( )
        # conn.close( )
        print("資料庫初始化完成")

init_db( )
