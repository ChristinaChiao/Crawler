import pandas as pd
import sqlite3

# 1. 準備一份爬蟲抓到的資料
new_data = {
    "title": ["Pandas"],
    "price": [1000],
    "views": [500]
}

df = pd.DataFrame(new_data)

print(df)

with sqlite3.connect("course_data.db") as conn:
    cursor = conn.cursor( )
    df.to_sql("courses", conn, if_exists="append", index=False)
    
