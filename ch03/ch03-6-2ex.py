import os

import matplotlib.pyplot as plt
import pandas as pd

# 1. 環境字型設定（避免中文與負號變方塊）
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 2. 讀取同一層資料夾的 CSV 檔案
#    VS Code 執行/除錯時的工作目錄（cwd）可能不是這支程式所在的資料夾，
#    用 __file__ 組出絕對路徑，不管從哪裡執行都能正確找到 CSV
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "3-6任務2.csv")
# __file__（起點：我自己）: 1005\HW3_02_2.py
# os.path.abspath(__file__)（第2層：我的絕對身分）: C:\venv_spider\python_idle\1005\HW3_02_2.py
# os.path.dirname(...)（第3層：我的家在哪裡）:C:\venv_spider\python_idle\1005\
# os.path.join(..., "3-6任務2.csv")（最外層：加上新目標）: C:\venv_spider\python_idle\1005\3-6任務2.csv
df = pd.read_csv(CSV_PATH, encoding="utf-8-sig")

# 3. 按「分店」分組，並計算「最高業績」與「最低業績」
df_summary = df.groupby("分店")["營收"].agg(最高業績="max", 最低業績="min")

# 4. 將統計結果繪製成「長條圖 (bar)」
df_summary.plot(kind="bar", title="各分店最高與最低業績摘要")

# 5. 圖表美化調整
plt.xticks(rotation=0)      # 讓 X 軸分店名稱保持水平
plt.ylabel("營收 (新台幣)")  # 補上 Y 軸單位
plt.tight_layout()          # 自動微調邊界，防文字被卡掉

# 6. 顯示圖表
plt.show()
