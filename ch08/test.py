# 💡 不需要 import requests 了，直接讀取本機檔案

# 1. 設定您的檔案路徑
file_path = 'c:/venvShao/PythonCode/ch08/comment.html'

# 2. 用 big5 編碼手動讀取這個檔案
with open(file_path, 'r', encoding='big5', errors='ignore') as f:
    html_content = f.read()

# 3. 將內容裡的 charset=Big5 改成 charset=utf-8 (讓瀏覽器知道它變 UTF-8 了)
html_content = html_content.replace('charset=Big5', 'charset=utf-8')
html_content = html_content.replace('charset=big5', 'charset=utf-8')

# 4. 把修正後的內容，覆蓋儲存回原本的檔案（指定用 utf-8 寫入）
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("檔案已成功轉換為 UTF-8 編碼，亂碼已修正！")
