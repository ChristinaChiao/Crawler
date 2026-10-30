##list1 = [10,30,60,20,50,40]
##print(list1)
##
##list2 = [10,30,60,20,50,40]
##
##list3 = [
##        [10,20,30],
##        [40,50,60]
##    ]

##news_titles = [ "台積電股價新高","AI概念股轉強","美股四大指數收紅" ]
##news_data = [ ["台積電股價新高",1500],
##              ["AI概念股轉強",800],
##              ["美股四大指數收紅",1200]
##              ]
##click_count = news_data[0][1] #第一個[0]列(橫)數第二個[1]行(直)數
##print(click_count)
##click_count = news_data[2][0] #美股四大指數收紅
##print(click_count)
##print(f"第三則新聞：{news_data[2][0]}")
##print("第三則新聞：", news_data[2][0])


##single_news = {
##    "title": "台積點股價新高",
##    "clicks": 1500,
##    "source":"財經日報"
##    }
##print("新聞標題：", single_news["title"])
##print("新聞來源：", single_news["source"])
##print("新聞來源：", single_news.get("source")) #安全取值

##all_news = [
##        {"title": "台積電", "price": 800, "rank":1},
##        {"title": "聯發科", "price": 1000, "rank":2},
##        {"title": "鴻海", "price": 150, "rank":3},
##    ]
##for item in all_news: #item代表每一個項目
##  print("標題：", item["title"]) #標題： 台積電
##  print("價格：", item["price"]) #價格： 800
##  print("排名：", item["rank"]) #排名： 1
##
##print("標題","\t","價格","\t","排名")
##for item in all_news:
##    print(item["title"],"\t",item["price"],"\t",item["rank"])

##cart = [
##        {"name": "Python 書", "price": 450, "count":1},
##        {"name": "無線滑鼠", "price": 890, "count":2},
##        {"name": "螢幕支架", "price": 1200, "count":1},
##    ]
##total_cost = 0
##for item in cart:
##    total = item["price"]
##    count = item["count"]
##    cost = total * count
##    print(item["name"],"總金額：",(cost))
##    total_cost+=cost
##print("總花費：", total_cost)
    

site_data = {"city":"Taipei","weather":
             [
                 {"time":"morning","temp":25},
                 {"time":"night","temp":18}
             ]
            }
for item in site_data:
     total = item["price"]
     count = item["temp"]
print("晚上的氣溫是",{site_data[1][1]}, "度")
