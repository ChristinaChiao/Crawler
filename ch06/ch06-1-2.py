import urllib.request
import re

url = "https://zh.wikipedia.org/zh-tw/Python"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    html_content = response.read().decode("utf-8")
    print(html_content)

result = re.sub(r"<table.*?>","\n",  html_content)
print(result)

with open("python_wikipedia.html", "w", encoding="utf-8") as file:
    file.write(html_content)