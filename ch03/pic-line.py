import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 

trend_data = {
    "日期": pd.to_datetime(["2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10"]),
    "業績": [12000, 15000, 11000, 18000, 22000]
}
df_trend = pd.DataFrame(trend_data)
# 開始畫圖 
df_trend.plot(x="日期", y="業績", kind="line", marker='o', title="本週業績趨勢圖") #曲線圖
plt.ylabel("新台幣")
plt.grid(True)
plt.show( )  
