# # 自訂完整 HTML + webview
import pandas as pd
import webview
import numpy as np

data = {
    "訂單編號": ["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "拿鐵咖啡", "美式咖啡", "卡布奇諾", None, "焦糖瑪奇朵"],
    "數量": [2, 1, 2, np.nan, 1, 3],
    "金額": [160, 120, 160, 120, 150, np.nan]
}

df = pd.DataFrame(data)

print("--- 原始髒資料 ---")
print(df)
print()
# 1. 
print(f"\n是否有重複資料：\n{df.duplicated( )}")

if df.duplicated( ).any():
    df_clean = df.drop_duplicates()
    print(df_clean)

print()
df_clean['品名'] = df_clean['品名'].fillna("未分類")

# avg_price = df_clean['數量'].mean() # 平均數
# df_clean['數量'] = df_clean['數量'].fillna(round(avg_price, 0))

median_quantity = df_clean['數量'].median() # 中位數
df_clean['數量'] = df_clean['數量'].fillna(median_quantity)

avg_price = df_clean['金額'].mean()
df_clean['金額'] = df_clean['金額'].fillna(avg_price)

print(df_clean)

# DataFrame → HTML table
table_html = df.to_html( 
    index=False,
    classes="paleBlueRows"
)


table2_html = df_clean.to_html(
    index=False,
    classes="paleBlueRows"
)

html =  f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    https://divtable.com/table-styler/

    <style>
        table.paleBlueRows {{
            font-family: "Times New Roman", Times, serif;
            border: 1px solid #FFFFFF;
            width: 350px;
            height: 200px;
            text-align: center;
            border-collapse: collapse;
        }}

        table.paleBlueRows td,
        table.paleBlueRows th {{
            border: 1px solid #FFFFFF;
            padding: 3px 2px;
        }}

        table.paleBlueRows tbody td {{
            font-size: 13px;
        }}

        table.paleBlueRows tr:nth-child(even) {{
            background: #D0E4F5;
        }}

        table.paleBlueRows thead {{
            background: #0B6FA4;
            border-bottom: 5px solid #FFFFFF;
        }}

        table.paleBlueRows thead th {{
            font-size: 17px;
            font-weight: bold;
            color: #FFFFFF;
            text-align: center;
            border-left: 2px solid #FFFFFF;
        }}

        table.paleBlueRows thead th:first-child {{
            border-left: none;
        }}

        table.paleBlueRows tfoot {{
            font-size: 14px;
            font-weight: bold;
            color: #333333;
            background: #D0E4F5;
            border-top: 3px solid #444444;
        }}

        table.paleBlueRows tfoot td {{
            font-size: 14px;
        }}
    </style>


</head>

<body>
    {table_html}
    <br>
    {table2_html}
</body>

</html>
"""


webview.create_window(
    "DataFrame 表格",
    html=html,
    width=600,
    height=400
)

webview.start()
