import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# 模擬連鎖店銷售明細
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "廣告費": [1000, 800, 1200, 1500, 1100, 1300],
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50],
    "消費金額": [100, 80, 120, 150, 110, 130],
}
df = pd.DataFrame(data)

# 任務：計算每個「區域」的「營收總和」與「平均每客單價」
summary = df.groupby("區域").agg({
    "營收": ["sum", "mean", "max", "min"],
    "客數": ["sum","mean"]
})

print("--- 區域營收摘要 ---")
print(summary)

# 顯示四個圖在同一個圖表視窗
numpy = np
fig, axarr = plt.subplots(2, 2, num="各區域營收與消費分析") # 顯示四個圖在同一個圖表視窗

#長條圖
df.plot(
    x="區域",
    y="營收",
    kind="bar",
    title="各區域營收",
    ax=axarr[0, 0]
)
axarr[0, 0].set_ylabel("營收")

# 圓餅圖
df.groupby("區域")["營收"].sum().plot(
    kind="pie",
    autopct="%1.1f%%",
    title="各區域營收占比",
    ax=axarr[0, 1]
)
axarr[0, 1].set_ylabel("")

#散佈圖 
df.plot(
    x="廣告費",
    y="營收",
    kind="scatter",
    title="廣告費與營收關係",
    ax=axarr[1, 0]
)

# 直方圖
df["消費金額"].plot(
    kind="hist",
    bins=10,
    title="客戶消費金額分布",
    ax=axarr[1, 1]
)
axarr[1, 1].set_xlabel("消費金額")

#其中要有下方四個圖表
fig.tight_layout()
plt.show()