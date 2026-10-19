import requests
from bs4 import BeautifulSoup

url = "http://example.com"

response = requests.get(url)
print(response)
html_doc = response.text
print(html_doc)
print("-"*50)
soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())
