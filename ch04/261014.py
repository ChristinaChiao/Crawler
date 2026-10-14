import re
#result = re.findall(r'.', 'This is a sample text with several words.')
#print(result)

result = re.findall(r'[^at]', 'This is a sample text with several words.')
print(result)

result = re.findall(r'.*', 'This is a sample text with several words.')
print(result)

result = re.findall(r'(text)+', 'This is a sample text with several words.')
print(result)

id_text = "我的身分證字號是A123456789"

#無論是用 re.findall 還是 re.search 都可以取得身分證資訊
print("使用 re.findall 取得身分證資訊")
result = re.findall(r'([A-Z])([12])(\d{8})', id_text)
print(result)
print("縣市代碼：", result[0][0] if result else None)
print("性別代碼：", result[0][1] if result else None)
print("流水號碼：", result[0][2] if result else None)
print("完整身分證號碼：", "".join(result[0]) if result else None)

print("使用 re.search 取得身分證資訊")
match = re.search(r'([A-Z])([12])\d{8}', id_text)
if match:
    # print(match.group(0))
    # print(match.group(1))
    # print(match.group(2))
    print("縣市代碼：", match.group(1))
    print("性別代碼：", match.group(2))
    print("流水號碼：", match.group(3))
    print("完整身分證號碼：", match.group(0))
else:
    print("No match found.")

