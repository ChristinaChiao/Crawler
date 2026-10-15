# 6-1-1
import http.client

url = "https://zh.wikipedia.org/zh-tw/Python"

conn = http.client.HTTPSConnection("zh.wikipedia.org")
conn.request("GET", "/wiki/Python")
response = conn.getresponse()
print("狀態：",response.status, "原因：", response.reason)
html_content = response.read().decode("utf-8")
print(html_content)