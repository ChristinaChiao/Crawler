#無使用pandas
raw_data = [
    {"item": "iPhone 15", "price": "$29,900"},
    {"item": "iPhone 15", "price": "$29,900"},
    {"item": "iPad Air", "price": "$19,500"},
    {"item": "MacBook", "price": "None"} # 缺失值
]

for item in raw_data:
   item["price"] = item["price"].replace("$", "").replace(",", "")
   print(item["price"])
   

# #單一一個數字變整數
# s = "$29,900" #字串有immutable特性(不可變)
# print(s.replace("$", "").replace(",", "")) #取代，不可以有空格，結果 29900
# print(s.replace("$", "")) #結果 29,900
# print(s.replace(",", "")) #結果 $29900
# s = s.replace("$", "").replace(",", "")
# print(s)

#------------------------------------------------------------------------------#

raw_data = [10,10,20,20,30,30,30,30] #data

# #刪除重複的元素(方法1)
# raw_data = list(set(raw_data)) #set轉集合，集合代表不能有重複，list用來轉回列表
# print(raw_data)

#刪除重複的元素(方法2)
for item in raw_data:
  count = raw_data.count(item)
  if count >= 2: #數字2的原因是至少有兩個重複的元素才需要刪除其中一個
      for i in range(count - 1):
          raw_data.remove(item)
print(raw_data)

# #刪除指定位置(最後一個)
# del raw_data[-1] 
# print(raw_data)

# #不考慮位置，直接刪除第一個匹配的元素
# raw_data.remove(10)
# print(raw_data)



