
import pandas as pd
import numpy as np
data = {
"訂單編號": ["1", "2", "1", "3", "4"],
"金額": [1200, 800, 1200, np.nan, 2500],
"狀態": ["已出貨", "處理中", "已出貨", "已出貨", "已出貨"]
}
raw_df = pd.DataFrame(data)
# 1. 刪除「訂單編號」重複的列
df_clean = raw_df.drop_duplicates(subset=["訂單編號"])
# 2. 將「金額」欄位的空值填補為該欄位的平均值
mean_value = df_clean["金額"].mean()
df_clean["金額"] = df_clean["金額"].fillna(mean_value)
# 3. 篩選出「金額 > 1000」且「狀態為 '已出貨'」的資料
result_df = df_clean[(df_clean["金額"] > 1000) & (df_clean["狀態"] == "已出貨")]
print(result_df)