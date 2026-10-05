import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定字體
df_trend = pd.read_csv("C:/venvShao/PythonCode/HW/HW-ch03-6-2.csv")

store_stats = df_trend.groupby("分店")["營收"].agg(
    最高營收="max",
    最低營收="min",
)

ax = store_stats.plot(
    kind="bar",
    title="各分店最高與最低營收",
    xlabel="分店",
    ylabel="營收",
)
ax.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.show()