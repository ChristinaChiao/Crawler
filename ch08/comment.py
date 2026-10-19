    # import bs4
    # from bs4 import BeautifulSoup
    # with open("c:/venvShao/PythonCode/ch08/comment.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()

    # soup = BeautifulSoup(html_content, "html.parser")

    # # 取得標題
    # title = soup.find("h3", class_="comment-item-header-title")
    # print(title.text)

    # #取得評論內容
    # comment = soup.find("div", class_="comment-item-subItem comment-item-detail")
    # for child in comment.children:
    #     if child.name == "p":
    #         print(child.text)

    # #法2
    # print(comment.p.text)

#擷取多個標題和評論內容
# import requests
# from bs4 import BeautifulSoup
# url = "https://www.gu-global.com/tw/zh_TW/product-detail.html?productCode=u0000000052759"
# response = requests.get(url)
# html_content = response.text
# soup = BeautifulSoup(html_content, "html.parser")
# comments = soup.find_all("article", class_="comment-item")

# for comment in comments:
#     title = comment.find("h3", class_="comment-item-header-title").text
#     content = comment.find("div", class_="comment-item-subItem comment-item-detail").p.text
#     print(f"標題: {title}")
#     print(f"內容: {content}")
#     print("-" * 40)

import bs4
from bs4 import BeautifulSoup
with open("c:/venvShao/PythonCode/ch08/task2.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, "html.parser")

#取得標題
title = soup.find("h3", class_="comment-item-header-title")
print(title.text)

#取得評論內容
comment = soup.find("div", class_="comment-item-subItem comment-item-detail")
#法1：使用 children 遍歷所有子節點，取得所有 p 標籤的內容
for child in comment.children:
    if child.name == "p":
        print(child.text)

#法2
print(comment.p.text)

#取得所有評論
comments = soup.find_all("article", class_="comment-item")
for comment in comments:
    title = comment.find("h3", class_="comment-item-header-title").text
    content = comment.find("div", class_="comment-item-subItem comment-item-detail").p.text
    print(f"標題: {title}")
    print(f"內容: {content}")
    print("-" * 40)
