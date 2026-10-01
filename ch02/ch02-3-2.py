import xml.etree.ElementTree as ET
xml_string = '''
<news_list>
  <item id="1">
      <title>Python爬蟲入門</title>
      <author>老師</author>
  </item>
  <item id="2">
      <title>AI時代來臨</title>
      <author>小助手</author>
  </item>
</news_list>
'''

root = ET.fromstring(xml_string)
print("---新聞列表---")

item_node = root.find("item") #尋找item標籤
print(item_node.tag)
print(item_node.get("id")) #看內部屬性的值

for news in root.findall("item"): #尋找所有item標籤
    print(news.tag, "id=", news.get("id"))
    print("標題=", news.find("title").text) 
    #靠news.find("title")尋找title標籤，.text取得標籤內的文字
    print("作者=", news.find("author").text) 
    #靠news.find("author")尋找author標籤，.text取得標籤內的文字