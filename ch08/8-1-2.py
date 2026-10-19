from bs4 import BeautifulSoup
html = """
<tr>
    <td class="label">姓名</td>
    <td class="value">張小明</td>
    <td class="label">職稱</td>
    <td class="value">工程師</td>
</tr>
"""

soup = BeautifulSoup(html, "html.parser")
tds = soup.find_all("td")
for td in tds:
    print(td.text)


