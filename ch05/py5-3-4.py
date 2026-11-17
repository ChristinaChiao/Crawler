import sqlite3

def dict_factory(cursor, row):
    """將回傳的每一列轉為字典的轉換器"""
    d = {}
    for idx, col in enumerate(cursor.description):
        print("col：", col)
        print(f"row[{idx}]",row[idx])
        d[col[0]] = row[idx] 
        # d["id"] = 1
        # d["title"] = "2026/4/16 爬蟲課綱更新"
    return d

with sqlite3.connect("news_data.db") as conn:
    # 注入轉換器
    conn.row_factory = dict_factory
    cursor = conn.cursor( )
    cursor.execute("SELECT * FROM news LIMIT 1")
    
    result = cursor.fetchone( )
    print(f"轉換後的字典結果: {result}")
    # 現在可以直接用 Key 存取：print(result['title'])
