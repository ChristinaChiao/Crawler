import pandas as pd
import sqlite3

# 1. 準備一份爬蟲抓到的資料
data = {
    "title": ["Python 爬蟲特訓", "AI 自動化實戰", "資料庫設計入門"],
    "price": [1200, 1500, 980],
    "views": [500, 1200, 300]
}

#雖然list也能建立DF，但不建議
# data = ["Python 爬蟲特訓", "AI 自動化實戰", "資料庫設計入門"]
df = pd.DataFrame(data)

# lis = [[10,20,30],
#        [40,50,60],
#        [70,80,90]]
# lis[0][2]

print(df)

with sqlite3.connect("course_data.db") as conn:
    cursor = conn.cursor( )
    df.to_sql("courses", conn, if_exists="replace", index=False)
    
