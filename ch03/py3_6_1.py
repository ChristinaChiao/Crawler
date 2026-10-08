import pandas as pd  # 匯入 pandas 庫，並簡稱為 pd，用於資料處理與分析

# 模擬連鎖店銷售明細的字典資料
# 包含四個欄位：'區域'、'店名'、'營收'、'客數'
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50],
}

df = pd.DataFrame(data)  # 將字典資料轉換為 pandas 的 DataFrame（二維表格結構）

# 任務：計算每個「區域」的「營收總和」、「營收平均」與「客數總和」
# groupby('區域')：依照「區域」欄位進行分組
# agg({...})：對不同的欄位套用不同的聚合函數
summary = df.groupby("區域").agg(
    {"營收": ["sum", "mean"], "客數": "sum"}  # 對「營收」欄位同時計算總和 (sum) 與平均 (mean)
)  # 對「客數」欄位計算總和 (sum)
#  "sum" 和 "mean" 不是 Python 原生的內建函式，而是 pandas 內部封裝（內建）的字串捷徑。
# 當資料表有很多欄位，而想對不同欄位做不同的統計時，就必須用字典 { 欄位名稱 : 計算公式 } 的方式來指定。
# groupby=欄位名稱，agg()中要計算的為列的名稱。

# # 寫法變更1：使用 NumPy 函式庫
# import numpy as np
# summary = df.groupby("區域").agg({"營收": [np.sum, np.mean], "客數": np.sum})

# # 寫法變更2：使用 Python 內建函式與 pandas 物件方法（此處的 sum 是 Python 內建，但 mean 必須用 pandas 的字串或 numpy 替代，因為 Python 沒有內建 mean 函式）
# summary = df.groupby("區域").agg({"營收": [sum, "mean"], "客數": sum})


print("--- 區域營收摘要 ---")  # 印出標題分隔線
print(summary)  # 印出計算好的彙總結果表
