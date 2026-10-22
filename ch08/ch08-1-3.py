from bs4 import BeautifulSoup

html = "<html><body><div><p><b id='target'>標籤文字</b></p></html>"

soup = BeautifulSoup(html, "html.parser")
target_tag = soup.find(id="target")
# print(target_tag.text)

# for parent in target_tag.parents:
#     print(parent.name)
    
print(soup.find("html"))
print()
print(soup.find("html").parent)