from bs4 import BeautifulSoup

# html = '<a href="https://example.com" class="link" id="target">點我前往</a>'
# soup = BeautifulSoup(html, 'html.parser')
# a_tag = soup.select_one("#target")

# url_a = a_tag['href']
# print(url_a)

# url_b = a_tag.get('href')
# print(url_b)


html = '<a class="link" id="target">點我前往</a>'
soup = BeautifulSoup(html, 'html.parser')
a_tag = soup.select_one("#target")

# url_a = a_tag['href']
# print(url_a) # KeyError because 'href' attribute is missing

url_b = a_tag.get('href')
print(url_b)