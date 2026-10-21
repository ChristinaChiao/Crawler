from bs4 import BeautifulSoup

# 8-1 選擇題第5題
# html = """
# <div id="content">
#     <h1 class="title">今日熱門商品</h1>
#     <ul class="item-list">
#         <li class="item hot">iPhone 15</li>
#         <li class="item">PS5 Slim</li>
#         <li class="item hot">RTX 4090</li>
#     </ul>
#     <p id="footer">最後更新：2026-04-22</p>
# </div>
# """
# soup = BeautifulSoup(html, 'html.parser')
# tag_all_li = soup.find('ul')
# print(list(tag_all_li.children)) #用來觀察包含的項目中也有換行符號等非標籤的內容

# tag_li = soup.select_one('ul.item-list > li')
# # print(tag_li)
# # print(tag_li.next_sibling) # 會取得下一個兄弟節點，可能是換行符號
# print(tag_li.find_next_sibling()) # 會取得下一個兄弟節點，忽略換行符號等非標籤內容


# 8-1 選擇題第6題
# find 與 select_one 的差異
# tag_li = soup.find('li', class_='item hot')
# print(tag_li)

# tag_li = soup.select_one('ul.item-list > li')
# print(tag_li)

# # 如果 find 找不到符合條件的標籤，會回傳 None
# target_tag = soup.find('li', class_='non-existent-class')
# print(target_tag.parent)

# # 如果 select_one 找不到符合條件的標籤，也會回傳 None
# target_tag = soup.select_one('li.non-existent-class')
# print(target_tag)



# 8-2 選擇題第6題
html = """
<div id="content">
    <h1 class="title">今日熱門商品</h1>
    <ul class="item-list">
        <li class="item hot">iPhone 15</li>
        <li class="item">PS5 Slim</li>
        <li class="item hot">RTX 4090</li>
        <li class="item">Core Ultra 7</li>
    </ul>
    <p id="footer">最後更新：2026-04-22</p>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')

result = soup.select(".item")
for item in result:
    print(item.get_text())
    
result = soup.select(".item1")
print(result)

result = soup.select_one(".item1")
print(result)