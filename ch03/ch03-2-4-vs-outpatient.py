#急診室outpatient範例
import pandas as pd
s = pd.Series([100, 200, 300], index=["台北", "台中", "高雄"])
print(s)
print(f"台中的數值是: {s['台中']}")
print(f"台北的數值是: {s['台北']}")
print(f"高雄的數值是: {s['高雄']}")

#使用pandas 讀取 outpatient.csv 檔案
df = pd.read_csv("C:/Users/User/venvShao/PythonCode/ch03/outpatient.csv")

#顯示csv裡面的roomname欄位，及regcount_person欄位
room = df['roomname']

person_max = df['regcount_person']
print("所有診室及掛號人數：",end="\n")#列出所有診室及掛號人數
print(pd.DataFrame({'roomname': room, 'regcount_person': person_max}))
#列出掛號人數最多的診室及人數
print(f"掛號人數最多的人數： {person_max.max()}") # 使用max()找到最大值
print(f"所有掛號人數及其索引：{list(person_max.items())}")
print(f"掛號人數最多的診室名稱： {room[person_max.idxmax()]}") # 使用idxmax()找到最大值的索引

regcount_list = list(person_max.items())
for item in regcount_list:
  index, value = item
  if value == person_max.max():
    print(f"掛號人數最多的診室及人數：{room[index]} - {value}")
    break
  
print(room[index])
print()

deptname = df['deptname']
print(deptname[index])
print()

#可以使用切片方式，列出前3筆資料。第一個項目是列，第二個項目是欄。
print(df[0:3])
print()

#使用iloc方式，列出前1筆資料
print(df.iloc[0:1])
print()

#使用iloc方式，列出第4筆資料,4代表索引位置3
print(df.iloc[3:4])
print()

#使用iloc方式，列出前4筆資料的第2到第5個欄位
print(df.iloc[1:5,1:5])
print()

#使用loc取得第3筆資料的roomname欄位值
print(df.loc[2 , 'roomname'], df.loc[2 , 'regcount_person'],"人")
print()
print(df.loc[2, ['roomname', 'regcount_person']])
print()
result = df.loc[df['deptname'].str.strip() == '板橋_眼科', ['roomname', 'regcount_person']] #用strip去空白
print(result)

#這種方式會顯示多餘的部分
print("眼科診室：", result['roomname'], ",掛號人數：", result['regcount_person'])
#正確寫法要用loc
print("眼科診室：", df.loc[df['deptname'].str.strip() == '板橋_眼科', ['roomname', 'regcount_person']])

print()
print(result.index)
i = list(result.index)[0]
print("列號", i)
print("眼科診室：", result.loc[i, 'roomname'], ",掛號人數：", result.loc[i, 'regcount_person'])