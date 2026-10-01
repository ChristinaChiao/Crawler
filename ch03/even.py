# 四個寫法-列印偶數列表
# 第一種是用for迴圈逐一判斷並列印
# 第二種是用for迴圈逐一判斷並存入列表
# 第三種是用列表生成式直接生成偶數列表
# 第四種是用列表生成式加條件判斷生成偶數列表
list1 = list(range(1,101))
list2 = []#空的可以裝東西
for i in list1:
    if i % 2 == 0:
        print(i, end=" ")
        list2.append(i)
print() #換行
print(list2) 

print() #換行
#comprehension
list3 = [x*2 for x in range(1, 51)]
print(list3) 

print() #換行
list4 = [x for x in range(1, 101) if x % 2 == 0]
print(list4) 

#直接用dataframe生成偶數列表
data=list(range(1, 101)) # 生成1到100的數據列表
import pandas as pd
df = pd.DataFrame(data)# 將數據列表轉換為DataFrame
df = df[df[0] % 2 == 0] # 篩選出偶數行,篩選方式是取餘數為0的行
print(df)
