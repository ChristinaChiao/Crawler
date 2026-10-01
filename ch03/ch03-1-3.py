#3-1-3
#合併多個資料
import pandas as pd

df1 = pd.DataFrame({"title":["新聞A"], "content":[100]})
print(df1)
df2 = pd.DataFrame({"title":["新聞B"], "content":[250]})
print(df2)

all_news = pd.concat([df1, df2], ignore_index=True) #ignore_index=True表示重新索引
print(all_news)



