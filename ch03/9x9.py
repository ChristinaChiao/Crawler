# 九九乘法表
for i in range(1,10):
  for j in range(1,10):
    print(f"{i}*{j}={i*j}", end="\t")
  print()
  
list1 = [[10,20,30], #list1[0]=[10,20,30]
         [40,50,60], #list1[1]=[40,50,60]
         [70,80,90]] #list1[2]=[70,80,90]
print(list1)
print(type(list1)) #印出list1的資料型態
#一個一個印出 
for item in list1: 
  for sub_item in item:
    print(sub_item)
print(type(item)) #印出每個子項目的資料型態
print(type(sub_item)) #印出每個子項目裡的元素的資料型態

#for i in list1[0]:
#  print(i, end=' ')
#for i in list1[1]:
#  print(i, end=' ')
#for i in list1[2]:
#  print(i, end=' ')
# 用巢狀迴圈印出 list1列表
for i in range(3):
  for j in range(i):
    print(j, end=" ")
  print()
  
# 用巢狀迴圈印出 list1 的元素
for i in range(len(list1)): #列數=len(list1)
  for j in range(len(list1[0])): #欄數=len(list[0])
    print(f"[{i}][{j}] = {list1[i][j]}", end="\t")
  print()