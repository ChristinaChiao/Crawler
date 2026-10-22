from bs4 import BeautifulSoup
html_doc = """
<div class="container">
    <h1 id="title">課程清單</h1>
    <ul class="course-list">
        <li>Python 基礎</li>
        <li>網路爬蟲實戰</li>
        <li>資料分析入門</li>
    </ul>
</div>
"""

soup = BeautifulSoup(html_doc, "html.parser")

list_tag = soup.find("ul")
print(f"ul元素：{list_tag}")
print("-"*50)
print(f"ul父節點：{list_tag.parent}")
print("-"*50)
print(f"ul父節點名稱：{list_tag.parent.name}")
print("-"*50)
for child in list_tag.children:
    if child.name:
        print(f"ul子節點：{child.name}, 內容：{child.text}")

print("-"*50)
print(list_tag.contents)
for content in list_tag.contents:
    if content.name:
        print(f"ul子節點（使用contents）：{content.name}, 內容：{content.text}")


