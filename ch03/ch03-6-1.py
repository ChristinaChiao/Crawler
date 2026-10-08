import pandas as pd

# 1. 建立包含「產品」、「單價」、「出口國」的原始資料（這裡以常見的貿易商品為例）
trade_data = {
    "產品": ["電子晶片", "精密螺絲", "感測元件", "綠能電池"],
    "單價": [120, 15, 80, 300],
    "出口國": ["美國", "德國", "日本", "越南"]
}
df_trade = pd.DataFrame(trade_data)

# 2. 匯出成名為 export_list.csv 的檔案
#    📌 index=False：要求不包含最左側的索引編號
#    📌 encoding="utf-8-sig"：關鍵！確保 Excel 開啟中文時不會產生亂碼
df_trade.to_csv("export_list.csv", index=False, encoding="utf-8-sig")

print("報表已成功匯出！請檢查您的專案資料夾下的 export_list.csv 檔案。")
