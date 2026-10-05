import re
phone_text = "門牌 123 號，電話 0912345678"
print(re.findall("\d+", phone_text))