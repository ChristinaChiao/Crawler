import re
import urllib.request

url= "https://zh.wikipedia.org/zh-tw/Python"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html_content = response.read().decode("utf-8")
    # print(html_content)

# result = re.sub(r"<table.*?>", "\n", html_content)
# print(result)

# with open("python_wikipedia.html", "w", encoding="utf-8") as file:
#     file.write("html_content")

# #從維基百科的python頁面中提取表格內容並將其換行顯示
# match = re.search(r"<table.*?>.*?</table>", html_content, re.S)
# if match:
#     table_content = match.group()
#     print(re.sub(r"<.*?>", "\n", table_content))

tables = re.findall(r"(<table class=\"wikitable\".*?</table>)", html_content, re.DOTALL)
print(len(tables))
print("-" * 50)
print(tables)
print("-" * 50)
result = re.sub(r"<.*?>", "", tables[0])
print(result.strip().replace("\n\n", " "))

with open("python_wikipedia.html", "w", encoding="utf-8") as file:
    file.write(html_content)

#找出HTML中的table表格內容
import re
html1 = """
<table><tbody><tr><td>Data</td></tr></tbody></table>
"""