import matplotlib.pyplot as plt  # 匯入 matplotlib 繪圖庫，用於畫折線圖、長條圖、圓餅圖等
import pandas as pd  # 匯入 pandas，用於建立 DataFrame 並直接呼叫 .plot() 畫圖
import tkinter as tk  # 匯入 tkinter，用於建立桌面視窗（GUI）

# -------------------- 【環境字型設定】 --------------------
# 📌 解決中文顯示問題：
# Matplotlib 預設字型不支援中文。如果不設定，圖表中的中文標題、軸標籤都會變成方塊（□）。
# 這裡指定使用 Windows 內建的標準中文字型「微軟正黑體」。
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 📌 解決負號變方塊的問題：
# Matplotlib 預設使用 Unicode 的標準負號（−），但多數中文字型不包含此符號，導致負數座標顯示出錯。
# 設定為 False 是強制停用 Unicode 負號，改用所有字型都支援的標準 ASCII 連字號（-）。
plt.rcParams['axes.unicode_minus'] = False

# -------------------- 【資料準備階段】 --------------------

# 📈 1. 趨勢資料（適用於：折線圖）
# 使用 pd.to_datetime 將字串格式的日期轉換為時間序列物件，這能讓 Matplotlib 自動優化 X 軸的時間軸間距。
trend_data = {
    "日期": pd.to_datetime(["2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10"]),
    "業績": [12000, 15000, 11000, 18000, 22000]
}
df_trend = pd.DataFrame(trend_data)


# 📊 2. 多維度業務資料（適用於：長條圖、圓餅圖、散佈圖）
# 同一個區域（如北區）出現兩次。我們特地加入了「月份」欄位，這樣在做長條圖時，
# 才能透過資料透視（Pivot）區分出 1 月與 2 月，避免兩筆北區資料重疊混淆。
region_data = {
    "月份": ["1月", "1月", "1月", "2月", "2月", "2月"],
    "區域": ["北區", "中區", "南區", "北區", "中區", "南區"],
    "營收": [30000, 25000, 20000, 35000, 30000, 25000],
    "廣告費": [5000, 4000, 3000, 6000, 5000, 4000]
}
df = pd.DataFrame(region_data)


# ⏳ 3. 客戶消費資料（適用於：直方圖）
# 純數值的單一欄位陣列，包含了 20 筆客戶消費金額，適合用來切成數個區間觀察人數分布（統計學中的次數分配）。
customer_data = {
    "消費金額": [320, 450, 500, 610, 700, 750, 800, 820, 900, 950,
               980, 1020, 1100, 1150, 1200, 1250, 1300, 1400, 1500, 1800]
}
df_customer = pd.DataFrame(customer_data)

# -------------------- 【圖表繪製函式集】 --------------------

# 1️⃣ 業績趨勢圖（折線圖）
def show_trend_chart():
    # 📌 清除畫布：防範疊圖發生的關鍵
    #plt.close('all')  
    
    # 📌 Pandas 內建繪圖：
    # kind="line" 產生折線圖；marker='o' 在每個數據節點點上圓圈，方便對照精準數值。
    # 備註：Pandas 這裡會自動把 "日期" 欄位當作 X 軸標籤（xlabel），所以後面不用再設定 xlabel。
    df_trend.plot(x="日期", y="業績", kind="line", marker='o', title="本週業績趨勢圖")
    
    # 📌 控制視窗標題：
    # 因為 df.plot() 會在後台自建視窗，必須透過 plt.gcf()（取得當前圖表物件）
    # 來控制並修改該彈出視窗的頂部標題。
    plt.gcf().canvas.manager.set_window_title("折線圖")  
    
    plt.ylabel("新台幣")       # 手動補上 Y 軸的貨幣單位
    plt.grid(True)            # 開啟背景格線，大幅提升數字對照的易讀性
    plt.tight_layout()        # 自動微調邊界，防止中文標題或文字被視窗邊緣吃掉
    plt.show()                # 正式彈出圖表視窗（注意：此時會阻塞 Tkinter 主執行緒，直到視窗被關閉）
    label4.config(text="已顯示：業績趨勢圖（折線圖）") # 更新 GUI 介面底部的狀態文字


# 2️⃣ 各區域營收（長條圖）
def show_bar_chart():
    # ⚠️ 注意：原程式這裡註解掉了 plt.close('all')，若連續點擊其他按鈕可能會產生畫布堆疊或殘留。
    
    # 📌 資料透視與分組繪圖（精華所在）：
    # df.pivot() 將流水帳表格轉換為「寬表格」：橫列(index)變成區域、直欄(columns)變成月份。
    # 轉換後呼叫 .plot(kind="bar")，Matplotlib 就會自動在 X 軸的每個區域旁，
    # 「並排」畫出 1 月與 2 月的不同顏色長條，並自動在右上角補上月份圖例。
    df.pivot(index="區域", columns="月份", values="營收").plot(kind="bar", title="各區域營收")
    # df.plot(x="區域", y="營收", kind="bar", title="各區域營收（不用 pivot 的慘狀）")
    plt.gcf().canvas.manager.set_window_title("長條圖")
    plt.ylabel("營收")
    
    # 📌 調整刻度角度：
    # 長條圖預設會把 X 軸的標籤（如：北區、中區）旋轉 90 度變垂直。
    # 因為中文字數很短，設定 rotation=0 讓字體維持水平，符合台灣人的閱讀習慣。
    plt.xticks(rotation=0)  
    
    plt.tight_layout()
    plt.show()
    label4.config(text="已顯示：各區域營收（長條圖）")


# 3️⃣ 各區域營收占比（圓餅圖）
def show_pie_chart():
    # 📌 顯示宣告物件導向寫法：
    # 圓餅圖如果不指定 fig, ax，Matplotlib 預設會在外圍畫一個正方形的座標外框與刻度，非常難看。
    # 這裡主動生成獨立的畫布(fig)與軸線(ax)，以便後面關閉這個外框。
    fig, ax = plt.subplots()
    
    # 📌 資料加總與繪圖：
    # 先用 groupby("區域")["營收"].sum() 把 1、2 月的營收合併，算出每個區域的總營收。
    # ax=ax：指定把這張圓餅圖填入我們剛才準備好的乾淨畫布中。
    # autopct="%1.1f%%"：自動計算百分比佔比，並格式化為顯示到小數點後第一位的字串（例如：35.5%）。
    df.groupby("區域")["營收"].sum().plot(
        ax=ax,
        kind="pie",
        autopct="%1.1f%%",  
        title="各區域營收占比"
    )
    
    # 📌 圓餅圖專屬美化：
    ax.axis("off")  # 關鍵：徹底隱藏圓餅圖後方的矩形座標軸、刻度線與外框(Pandas 和 Matplotlib 幫您預先關掉了外框；雙重保險)
    fig.canvas.manager.set_window_title("圓餅圖")
    
    # loc="best"：讓系統自動尋找圖表中最空曠、不會擋到圓餅圖的角落來放置圖例
    ax.legend(loc="best")  
    
    plt.tight_layout()
    plt.show()
    label4.config(text="已顯示：各區域營收占比（圓餅圖）")


# 4️⃣ 廣告費與營收關係（散佈圖）
def show_scatter_chart():
    # 📌 關聯性分析：
    # kind="scatter" 用於繪製散佈圖（點狀圖）。
    # 將廣告費設為 X 軸、營收設為 Y 軸，用來觀察這兩個變數之間是否存在正相關（點的走向是否往右上方延伸）。
    df.plot(x="廣告費", y="營收", kind="scatter", title="廣告費與營收關係")
    
    plt.gcf().canvas.manager.set_window_title("散佈圖")
    plt.tight_layout()
    plt.show()
    label4.config(text="已顯示：廣告費與營收關係（散佈圖）")


# 5️⃣ 客戶消費金額分布（直方圖）
def show_hist_chart():
    # 📌 區間次數統計：
    # kind="hist" 繪製直方圖（次數分配圖）；bins=10 代表把消費金額的最大值到最小值之間，
    # 等距離切成 10 個區間（例如：300~450、450~600 ...），並自動統計落在各區間內的人數（次數）。
    df_customer["消費金額"].plot(kind="hist", bins=10, title="客戶消費金額分布")
    # 最低消費是 320 元，最高消費是 1800 元。當您設定 bins=10 時，Pandas 會自動在幕後做數學題：(1800-320)/10 = 148，每個區間寬度為 148 元。148 是「組距」（每個區間的寬度）。在圖表上，它代表每一根藍色柱子的橫向寬度。
    plt.gcf().canvas.manager.set_window_title("直方圖")
    plt.xlabel("消費金額")  # 直方圖預設不會幫 X 軸命名，這裡手動補上
    plt.ylabel("人數")      # 直方圖預設 Y 軸標籤是 "Frequency"，這裡將它中文化改為 "人數"
    
    plt.tight_layout()
    plt.show()
    label4.config(text="已顯示：客戶消費金額分布（直方圖）")

# -------------------- 【Tkinter 介面排版】 --------------------

root = tk.Tk()              # 初始化 Tkinter，建立最底層的主視窗物件
root.geometry("400x300")    # 設定主視窗的啟動解析度為 寬 400 像素 x 高 300 像素
root.title("業績圖表小工具")  # 設定主視窗左上角的標題文字

# 建立兩個文字標籤（Label），用來提示使用者與顯示點擊後的狀態回饋
label = tk.Label(root, text="請選擇要查看的圖表")
label4 = tk.Label(root, text="顯示結果")

# 📌 建立五顆功能按鈕（Button）：
# width=24：統一所有按鈕的寬度，讓視覺畫面排版看起來更整齊。
# command=show_xxx：這是最重要的參數！當使用者按下按鈕時，Tkinter 就會去執行對應的繪圖函式。
btn_trend = tk.Button(root, text="業績趨勢（折線圖）", width=24, command=show_trend_chart)
btn_bar = tk.Button(root, text="各區域營收（長條圖）", width=24, command=show_bar_chart)
btn_pie = tk.Button(root, text="營收占比（圓餅圖）", width=24, command=show_pie_chart)
btn_scatter = tk.Button(root, text="廣告費與營收（散佈圖）", width=24, command=show_scatter_chart)
btn_hist = tk.Button(root, text="消費金額分布（直方圖）", width=24, command=show_hist_chart)

# 📌 元件定位（Pack 垂直打包佈局）：
# pack() 會將元件由上到下依序塞入視窗中。
# pady=(上距, 下距)：代表元件外部的垂直留白距離（像素）。
# 例如 label.pack(pady=(20, 0)) 代表這個標籤距離頂端視窗邊緣 20 像素，下方與下一個元件不留白。
label.pack(pady=(20, 0))  
btn_trend.pack(pady=(20, 0))  # 第一顆按鈕距離上方標籤稍微拉開 20 像素
btn_bar.pack(pady=(10, 0))    # 後續按鈕之間固定保持 10 像素的間距
btn_pie.pack(pady=(10, 0))
btn_scatter.pack(pady=(10, 0))
btn_hist.pack(pady=(10, 0))
label4.pack(pady=(20, 0))     # 最底部的狀態標籤拉開 20 像素，與最後一顆按鈕區隔開來

# 💡 註解小補充（關於程式碼最後一行的提示）：
# padx=(a, b) 的寫法代表「左邊留白 a 像素，右邊留白 b 像素」，適用於水平排版（如橫向並排按鈕時）。

root.mainloop()  # 進入 Tkinter 的無限事件監聽迴圈。
                 # 程式會在這裡停住並保持視窗開啟，持續監聽滑鼠點擊事件，直到使用者按下 X 關閉視窗。
