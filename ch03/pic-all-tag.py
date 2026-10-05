import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# 模擬連鎖店銷售明細
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "廣告費":[1000, 600, 900, 1200, 1040, 960], 
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50],
    "消費金額":[3500, 2500, 3200, 4500, 3600, 3300], 
}
df = pd.DataFrame(data)


#Tkinter GUI介面
root = tk.Tk()
root.title("連鎖店銷售分析")
root.geometry("800x600")

#按鈕區
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

#圖表區
chart_frame = tk.Frame(root)
chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)   

#顯示圖表函式


trend_data = {
    "日期": pd.to_datetime(["2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10"]),
    "業績": [12000, 15000, 11000, 18000, 22000]
}
df_trend = pd.DataFrame(trend_data)


# 折線圖
def line_chart():
    fig, ax = plt.subplots(figsize=(8, 6))
    df_trend.plot(
        x="日期",
        y="業績",
        kind="line",
        marker='o',
        title="本週業績趨勢圖",
        ax=ax
    )
    ax.set_ylabel("新台幣")
    ax.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)

# 長條圖
def bar_chart():
    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot(
        x="區域",
        y="營收",
        kind="bar",
        title="各區域營收",
        ax=ax
    )

    ax.set_ylabel("營收")
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)


# 圓餅圖
def pie_chart():
    fig, ax = plt.subplots(figsize=(8, 6))
    df.groupby("區域")["營收"].sum().plot(
        kind="pie",
        autopct="%1.1f%%",
        title="各區域營收占比",
        ax=ax
    )

    ax.set_ylabel("")
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)

#散佈圖 
def scatter_chart():
    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot(
        x="廣告費",
        y="營收",
        kind="scatter",
        title="廣告費與營收關係",
        ax=ax
    )

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)

# 直方圖
def hist_chart():
    #建立 Figure 和 Axes
    fig, ax = plt.subplots(figsize=(8, 6))

    df["消費金額"].plot(
        kind="hist",
        bins=10,
        title="客戶消費金額分布",
        ax=ax
    )

    ax.set_xlabel("消費金額")
    ax.set_ylabel("頻率")

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP,  expand=True)
    
#按鈕
button = tk.Button(button_frame, text="折線圖", font=("微軟正黑體", 16), command=line_chart)
button.pack(side=tk.LEFT, padx=(10,0))

button1 = tk.Button(button_frame, text="長條圖", font=("微軟正黑體", 16), command=bar_chart)
button1.pack(side=tk.LEFT, padx=(10,0))

button2 = tk.Button(button_frame, text="圓餅圖", font=("微軟正黑體", 16),command=pie_chart)
button2.pack(side=tk.LEFT, padx=(10,0))

button3 = tk.Button(button_frame, text="散佈圖", font=("微軟正黑體", 16), command=scatter_chart)
button3.pack(side=tk.LEFT, padx=(10,0))

button4 = tk.Button(button_frame, text="直方圖", font=("微軟正黑體", 16), command=hist_chart)
button4.pack(side=tk.LEFT, padx=(10,0))

root.mainloop()
