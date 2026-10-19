from bs4 import BeautifulSoup

html="""
<tr>
    <td class="label">姓名</td>
    <div>其他</div>
    <td class="value">張小明</td>
    <td class="label">職稱</td>
    <td class="value">工程師</td>
</tr>
"""
soup = BeautifulSoup(html, "html.parser")
first_td = soup.find("td")
# print(first_td)

# next_td = first_td.find_next_sibling() #未指定
# print(next_td)

# next_td = first_td.find_next_sibling("td") # 指定尋找下一個 td 標籤
# print(next_td)

# 法1：找出其餘的兄弟節點 (td)
# for i in range(3):
#     next_td = first_td.find_next_sibling("td")
#     print(next_td)
#     first_td = next_td
    
# while True:
#     next_td = first_td.find_next_sibling("td")
#     if not next_td:
#         break
#     print(next_td)
#     first_td = next_td
    
# 法2：使用 find_all 找出所有 td 標籤
all_td = soup.find_all("td")
for td in all_td:
    print(td)