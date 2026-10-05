import re


text = "我的電話是 0912-345-678， ID是 WORKER_007"

print(re.findall("\d", text))

print(re.findall("\d\d\d", text))