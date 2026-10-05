import re
text = "我的電話是0912-345-678， ID是worker_007"
print(re.findall("\d", text))
print(re.findall("\d\d\d", text))
print(re.findall("\d\d\d-\d\d\d", text))