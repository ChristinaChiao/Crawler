#xml.etree.ElementTree模組提供了簡單的API來解析和創建XML數據。
#它允許你讀取、修改和生成XML文檔，並提供了方便的方法來遍歷和操作XML元素。
import xml.etree.ElementTree as ET
xml_data = '''
  <weather_report> 
    <city name="台北">
      <temp>25</temp>
      <status>雨</status>
    </city>
  </weather_report>
''' #自定義標籤
root = ET.fromstring(xml_data)
print(root.tag) #weather_report
city_node = root.find("city") #尋找city標籤
print(city_node.get("name")) #看內部屬性的值

temp_node = city_node.find("temp") #尋找temp標籤，不能用root
print("溫度：", temp_node.text) #溫度： 25