from bs4 import BeautifulSoup

html = """
<div id="content">
    <h1 class="title">今日熱門商品</h1>
    <ul class="item-list">
        <li class="item hot">iPhone 15</li>
        <li class="item">PS5 Slim</li>
        <li class="item hot">RTX 4090</li>
    </ul>
    <p id="footer">最後更新：2026-04-22</p>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')







html_with_links = """
<div class="menu">
    <a href="/news">新聞</a>
    <a href="https://google.com" target="_blank">外部連結</a>
    <a href="https://microsoft.com" target="_blank">外部連結</a>
    <a href="https://apple.com" target="_blank">外部連結</a>
    <a href="/about">關於我們</a>
</div>
"""
soup = BeautifulSoup(html_with_links, 'html.parser')
external = soup.select('a[target]')
#print(external)
for link in external:
    print(link.text)
    print(link['href'])

#請找出Task2.html中所有的<a>超連結
soup = BeautifulSoup(open("Task2.html", encoding="utf-8"), 'html.parser')
links = soup.select('a')
for link in links:
    print(link.text)
    print(link['href'])
