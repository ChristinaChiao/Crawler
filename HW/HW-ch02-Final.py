import pandas as pd

json_data = [{"name": "小明", "score": 85},
             {"name": "小華", "score": 92},
             {"name": "小美", "score": 78}]

# 解析 JSON 並轉為 DataFrame
df = pd.DataFrame(json_data)

# 重命名欄位名稱為「姓名」與「成績」
df = df.rename(columns={'name': '姓名', 'score': '成績'})

# 匯出 CSV 檔案
df.to_csv('E:/USB/c/使用者/User/venvShao/PythonCode/HW/students.csv', index=False, encoding='utf-8-sig')

print("已成功匯出 students.csv！")