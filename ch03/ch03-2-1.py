import pandas as pd
data = {
  "日期": ["2024-06-01", "2024-06-02", "2024-06-03", "2024-06-04", "2024-06-05", "2024-06-06"], 
  "收盤價": [800, 815, 802, 795, 1000, 900],
  "帳跌": [5, 5, -10, -5, -5, -100]
  
}

df = pd.DataFrame(data)
print("--股票小表格--")
print(df)

print("\n--- 僅觀察收盤價欄位(Series) ---")
print(df["收盤價"])

#判斷下跌的收盤價,並印出價格
down_box = list(pd.Series(data["帳跌"])<0) #pd.Series是將資料轉換成Series物件
print(df["收盤價"][down_box])

print(df[df["帳跌"]<0])
  
df = df[df["帳跌"]<0]
print(df["收盤價"])