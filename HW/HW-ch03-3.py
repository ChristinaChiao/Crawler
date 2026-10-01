raw_data = {
    "產品": ["拿鐵", "卡布奇諾", "美式咖啡", "摩卡", "焦糖瑪奇朵"],
    "價格": [120, 130, 100, 150, 160],
    "庫存": [50, 30, 80, 20, 10]
}
#1：精準定位修改
#將美式咖啡的價格修改為125，並印出
import pandas as pd
df = pd.DataFrame(raw_data)
#法1
df.loc[df["產品"] == "美式咖啡", "庫存"] = 80
print(df)
print("-"*50)

#法2
result = df[df["產品"] == "美式咖啡"]
print(result)
print(result['庫存'].values)
result['庫存'] = 120
print(result['庫存'])
print("-"*50)

#2：複雜篩選
#價格100-150之間，庫存低於40
filtered_df = df[(df["價格"] >= 100) & (df["價格"] <= 150) & (df["庫存"] < 40)]
print(filtered_df)

