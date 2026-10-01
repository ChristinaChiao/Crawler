#使用pandas
import pandas as pd
raw_data = [
    {"item": "iPhone 15", "price": "$29,900"},
    {"item": "iPhone 15", "price": "$29,900"},
    {"item": "iPad Air", "price": "$19,500"},
    {"item": "MacBook", "price": "None"} # 缺失值
]

df = pd.DataFrame(raw_data) #最適合處理 list+dict 格式的資料
print(df)

# 純字典的資料無法使用 DataFrame 直接轉換，因為 DataFrame 最適合處理 list+dict 格式的資料
# df2 = pd.DataFrame({"item": "iPhone 15", "price": "$29,900"})
# print(df2)
# df3 = pd.DataFrame([10,30,60,50,40]) #純 list 的資料也可以轉換成 DataFrame
# print(df3)
# DataFrame和python字串都是immutable（不可變）的資料結構

df = df.drop_duplicates() #若有重複的資料，會被移除，編號會不連續
print(df)

df = df.reset_index(drop=True) #重設索引，編號會連續
print(df)

df['price'] = df['price'].str.replace("$", "").str.replace(",", "")
print(df)

df['price'] = pd.to_numeric(df['price'], errors='coerce') #將字串轉換成數值，無法轉換的會變成 NaN
print(df)