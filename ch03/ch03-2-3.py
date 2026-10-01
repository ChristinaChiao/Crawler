import pandas as pd
data = {
  "日期": ["2024-06-01", "2024-06-02", "2024-06-03", "2024-06-04", "2024-06-05", "2024-06-06"], 
  "收盤價": [800, 815, 802, 795, 1000, 900],
  "帳跌": [5, 5, -10, -5, -5, -100]
  
}

df = pd.DataFrame(data)

print("前兩筆資料：",end="\n")
print(df.head(2))
print()
print("最後一筆資料：",end="\n")
print(df.tail(1))
print()
print("隨機兩筆資料：",end="\n")
print(df.sample(2))
print()
print("描述與數學相關的統計資料：",end="\n")
print(df.describe())
print()
print("資料摘要資訊：",end="\n")
print(df.info())
