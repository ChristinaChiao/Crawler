import re
#01
html_data = "價格:500元，價格:1200元，價格：80元"
re_with_group = re.findall(r'價格：\d+元', html_data)
print(re_with_group)

#02
html_data = "價格:500元，價格:1200元，價格：80元，電話：0912345678"
#限定在價格部份的數字
re_with_group = re.findall(r'價格：(\d+)元', html_data)
print(re_with_group)

#不限定在價格部份的數字
re_with_group = re.findall(r'(\d+)', html_data)
print(re_with_group)

#03
html_data = "蘋果：100元，香蕉：50元，橘子：80元"
#限定在價格部份的數字
re_with_group = re.findall(r'(\w+)：(\d+)元', html_data)
print(re_with_group)
