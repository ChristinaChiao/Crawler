import pandas as pd
import sqlite3

with sqlite3.connect("course_data.db") as conn:
    sql = "SELECT * FROM courses WHERE price > 1000"
    result = pd.read_sql(sql, conn) #result 是個DF
    print(result)
    

# 練習：利用pandas來刪除sqlite特定的資料
    result.to_sql("courses", conn, if_exists="replace", index=False)