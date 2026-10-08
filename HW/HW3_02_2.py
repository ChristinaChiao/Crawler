import pandas as pd

# 題目給定的原始資料準備
sales_data = {
    "日期": ["2026-01-10", "2026-01-15", "2026-02-05", "2026-03-12"],
    "營收": [5000, 7000, 4500, 8800]
}
df_sales = pd.DataFrame(sales_data)


# -------------------- 【開始執行時間趨勢分析步驟】 --------------------

# 1. 將「日期」轉為 Datetime 格式
df_sales["日期"] = pd.to_datetime(df_sales["日期"])


# 2. 新增一欄「月份」
#    📌 利用 .dt.month 屬性，自動從 Datetime 物件中提煉出月份數字（如 1, 2, 3）
df_sales["月份"] = df_sales["日期"].dt.month


# 3. 統計並印出「各月份」的營收總和
#    📌 按「月份」分組，並針對「營收」欄位呼叫 .sum() 加總
# 修改前：df_sales.groupby("月份")["營收"].sum()
# 修改後：
df_monthly_revenue = df_sales.groupby("月份")["營收"].sum().reset_index()
# 加上 .reset_index()，可以把 Series 強制轉換回 DataFrame（二維資料表） 格式。DataFrame 在列印時絕對不會出現 Name 和 dtype。
print(df_monthly_revenue)

# 執行 df_sales.groupby("月份")["營收"].sum() 時，輸出的結果本質上是一個 Pandas Series（一維數列物件），而不是一般的純文字。但呼叫了 groupby("月份")後，Pandas 幫你把原本的「月份」抽出來升格變成了這組數據的「索引（Index）」。所以右邊的營收數字只有一整條（一維），左邊則是對應的名字！