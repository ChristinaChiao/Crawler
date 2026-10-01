import pandas as pd
import numpy as np
raw_data = {
    "訂單編號":["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "卡布奇諾", "美式咖啡", None , "焦糖瑪奇朵"],
    "價格": [120, 130, 100, 150, np.nan],
    "庫存": [50, 30, np.nan , 20, 10]
}
#1：精準定位修改
#將美式咖啡的價格修改為125，並印出
df = pd.DataFrame(raw_data)
print("原始髒資料")
print(df)

#1
print(f"\n 是否有重複資料: \n{df.duplicated()}")

if df.duplicated().any():
    df_clean = df.drop_duplicates()
    print(df_clean)

print()
df_clean["品名"] = df_clean["品名"].fillna("未分類")
df_clean["價格"] = df_clean["價格"].fillna(0)
df_clean["庫存"] = df_clean["庫存"].fillna(0)

median_quantity = df_clean["庫存"].median() # 計算庫存的中位數
df_clean["庫存"] = df_clean["庫存"].fillna(median_quantity) # 將庫存中的缺失值填補為中位數

avg_price = df_clean["價格"].mean() # 計算價格的平均值
df_clean["價格"] = df_clean["價格"].fillna(avg_price) # 將價格中的缺失值填補為平均值


print(df_clean)