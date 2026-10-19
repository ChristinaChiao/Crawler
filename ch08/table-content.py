import pandas as pd

list1 = ["Header1", "Header2", "Header3"]
list2 = ["Data1", "Data2", "Data3"]

df = pd.DataFrame([list2], columns=list1)
print(df)

#找出標題欄位
import requests
from bs4 import BeautifulSoup

def get_table_content(tag_name):
    with open("table.html", "r", encoding="utf-8") as file:
        html_doc = file.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        tag_list = soup.find_all(tag_name)
        for tag in tag_list:
            print(tag.text)

get_table_content("th")
print("-"*50)

#找出td內容
get_table_content("td")
print("-"*50)

#表格內容轉換成DataFrame
def table_to_dataframe():
    with open("table.html", "r", encoding="utf-8") as file:
        html_doc = file.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        headers = [th.text for th in soup.find_all("th")]
        rows = []
        for tr in soup.find_all("tr"):
            cells = [td.text for td in tr.find_all("td")]
            if cells:
                rows.append(cells)
        return pd.DataFrame(rows, columns=headers)

df_from_html = table_to_dataframe()
print(df_from_html)