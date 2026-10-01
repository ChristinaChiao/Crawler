import tkinter as tk

def click():
    click.count += 1
    print("Clicked")
    label4["text"] ="按鈕被點了{}次".format(click.count)

click.count = 0
root = tk.Tk()
root.geometry("600x500") #設定視窗大小
label = tk.Label(root, text="這是我的第一個視窗")
label2 = tk.Label(root, text="這是第2個視窗")
label3 = tk.Label(root, text="這是第3個視窗")
label4 = tk.Label(root, text="顯示結果")

button = tk.Button(root, text="送出", width=20, command=click)

#設定排版
label.pack(pady = (50,0)) #上距離50，下距離0
label2.pack(pady = 50) #上距離50，下距離50
label3.pack(pady = 50)
button.pack(pady = (0,0)) #上距離0，下距離0
label4.pack(pady = 50)

root.mainloop()