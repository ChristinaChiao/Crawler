# 任務：從維基百科的Python頁面中提取表格內容並將其換行顯示
import urllib.request
import re
from bs4 import BeautifulSoup

url = "https://zh.wikipedia.org/zh-tw/Python"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    html_content = response.read().decode("utf-8")
##    print(html_content)

tables = re.findall(r'(<table class="wikitable">.*?</table>)',  html_content, re.DOTALL)
print(len(tables))
print("-"*50)
print(tables[0])
print("-"*50)
result = re.sub(r"<.*?>","",  tables[0])

# 使用BeautifulSoup解析提取的表格內容，請修改為解析<table>標籤而不是<ul>標籤
soup = BeautifulSoup(result, "html.parser")

list_tag = soup.find("ul")
print(f"ul父節點：{list_tag.parent.name}")

for child in list_tag.children:
    if child.name:
        print(f"ul子節點：{child.name}, 內容：{child.text}")