import requests
import re
url="https://www.megabank.com.tw/abroad-page/silicon-valley/zh-tw/contact-us"

res = requests.get(url)
html = res.text
print(html)

#任務一：從網頁中提取所有的電子郵件地址(限用RE模組)
emails = re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,}", res.text)
print(emails)

#任務二：從網頁中提取所有的電話號碼(限用RE模組)
phones = re.findall(r"\d{4}-\d{3}-\d{3}", res.text)
phones2 = re.findall(r"\d{2}-\d{4}-\d{4}", res.text)
print(phones)
print(phones2)

phones = re.findall(r"\d{2,4}-\d{3,4}-\d{3,4}", res.text) #合併寫法
print(phones)

