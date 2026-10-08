import re

text = "電話：0912345678"
# pattern = "\d+"
pattern = "[0-6]+"

print(re.findall(pattern, text))