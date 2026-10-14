import re  

#4-4-1
html_raw = "<div>歡迎來到<span class='highlight'>爬蟲教室</span></div>"

#提取span標籤內的內容
result = re.sub(r"<.*?>", "", html_raw)
print(result)

print()

#4-4-2 少了?的後果
bad_clean = re.sub(r"<.*>", "", html_raw)
print(bad_clean)

#4-4-3
result = re.sub(r"<.*?>", "\n", html_raw)
print(result)

    