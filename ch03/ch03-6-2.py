import matplotlib.pyplot as plt
import pandas as pd

# 解決中文顯示與負號變方塊的問題
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 模擬建立題目的原始資料 df (包含 分店、日期、營收)
restaurant_data = {
    "分店": ["台北店", "台中店", "高雄店", "台北店", "台中店", "高雄店"],
    "日期": ["2026-10-01", "2026-10-01", "2026-10-01", "2026-10-02", "2026-10-02", "2026-10-02"],
    "營收": [5000, 7000, 6000, 8000, 7500, 6500],
}
df = pd.DataFrame(restaurant_data)

# 2. 關鍵步驟：按「分店」分組，並同時算出「最高業績」與「最低業績」
#    使用剛剛選擇題學到的 .agg()，並自訂欄位名稱為「最高業績」與「最低業績」
df_summary = df.groupby("分店")["營收"].agg(最高業績="max", 最低業績="min")

# 3. 將此統計結果畫成一張「長條圖 (bar)」
df_summary.plot(kind="bar", title="各分店最高與最低業績摘要")

# 美化調整：讓 X 軸的店名保持水平不旋轉，並補上 Y 軸標籤
plt.xticks(rotation=0)
plt.ylabel("營收 (新台幣)")
plt.tight_layout()

# 顯示圖表
plt.show()
