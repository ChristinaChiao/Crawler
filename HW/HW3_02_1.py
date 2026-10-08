import pandas as pd
import numpy as np

# 題目給定的原始資料準備
data = {
    "訂單編號": ["1", "2", "1", "3", "4"],
    "金額": [1200, 800, 1200, np.nan, 2500],
    "狀態": ["已出貨", "處理中", "已出貨", "已出貨", "已出貨"]
}
raw_df = pd.DataFrame(data)


# -------------------- 【開始執行資料清洗步驟】 --------------------

# 1. 刪除「訂單編號」重複的列
#    📌 使用 subset 指定特定欄位，並用 inplace=True 直接修改原資料
raw_df.drop_duplicates(subset=["訂單編號"], inplace=True)


# 2. 將「金額」欄位的空值填補為該欄位的平均值
#    📌 先算出金額平均值，再用 fillna() 搭配 inplace=True 進行填補
mean_value = raw_df["金額"].mean()
raw_df["金額"].fillna(mean_value, inplace=True)


# 3. 篩選出「金額 > 1000」且「狀態為 '已出貨'」的資料
#    📌 使用 & 運算子連結多個條件，並記得每個條件要用小括號 ( ) 包起來
final_df = raw_df[(raw_df["金額"] > 1000) & (raw_df["狀態"] == "已出貨")]


# 顯示最終清洗與篩選後的結果
print(final_df)
