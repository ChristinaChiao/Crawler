import pandas as pd
df = pd.read_csv("E:/USB/c/使用者/User/venvShao/PythonCode/ch03/ch03-3-1.csv", header=None)
print(df)
print("-"*50)
print(df[0]) # 印出第一欄的資料
print("-"*50)
print(df.values[0]) # 印出第一列的資料
print("-"*50)
print(df.iloc[0]) # 印出第一列的資料
print("-"*50)
print(df.iloc[0,1]) # 印出第一列第一欄的資料
print("-"*50)

for i in range(3):
    for j in range(3):
        print(df.iloc[i,j], end=" ")
    print()
print("-"*50)

r,c = df.shape
for i in range(r):
    for j in range(c):
        print(f"df.iloc[{i},{j}] = {df.iloc[i,j]}", end="\t")
    print()
print("-"*50)

#10,20,30
#40 50 60
#70 80 90
#iloc 想抓出df子集
#50 60
#80 90

print(df.iloc[1:3,1:3]) # 印出子集 50 60 / 80 90
print("-"*50)

print(df.iloc[1:2,1:2]) # 印出子集 50

#iloc的使用
print("-"*17, "iloc的使用範例", "-"*17)
print(df.iloc[0])
print("-"*50)
print(*df.iloc[0])
print("-"*50)
print(df.iloc[0,1])

#loc的使用
print("-"*17, "loc的使用範例", "-"*17)
print(df.loc[0])
print("-"*50)
print(*df.loc[0])
print("-"*50)
print(df.loc[0,1])
print("-"*50)

df.columns = ["col1","col2","col3"]
df.index = ["row1","row2","row3"]
print(df)
print("-"*17, "loc 的真正使用", "-"*17)
print(df.loc['row1'])
print("-"*50)
print(*df.loc['row1'])
print("-"*50)
print(df.loc['row1':'row2'])
print("-"*50)


print(df.loc[df['col2'] > 50, :]) #針對某些列且所有欄位皆大於50
print("-"*50)

print(df.loc[df['col2'] > 40]) #針對某些列且所有欄位皆大於40

# 篩選 col2 大於 40 的列，並取得 col3 的資料
result = df.loc[df['col2'] > 40]
print(result)
print()
print(result['col3'])

result = df.loc[df['col2'] > 40, 'col3']
print(result)

s1 = "ABCDEF"
s1[:3] #效果同 s1[0:3]，會取得前三個字元 "ABC"
s1[3:] #效果同 s1[3:6]，s1[3:len(s1)]會取得後三個字元 "DEF"