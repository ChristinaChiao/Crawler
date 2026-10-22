def generate_search_url(base_url, keyword):
    from urllib.parse import quote
    encode_keyword = quote(keyword)
    return f"{base_url}/search?p={encode_keyword}"

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

#實測
yahoo_base = "https://tw.news.yahoo.com"
my_keyword = "颱風"
url = generate_search_url(yahoo_base, my_keyword)
print(f'生成的網址: {url}')

response = requests.get(url, headers=headers)
print(response.text)

#任務1：利用beautifulsoup 解析YAHOO新聞搜尋結果或 lxml 的xpath解析
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('h3 a')
for article in articles:
    print(article.text, article['href'])

#任務2：將解析後的新聞標題與連結存成清單(list)
news_list = []
for article in articles:
    news_list.append({
        'title': article.text,
        'link': article['href']
    })
print(news_list)


