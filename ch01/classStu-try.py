#寫法1
import classStudent #模組名稱
s1 = classStudent.student("李國毅", 35, "0912345678")
s1.take_exam() 

#寫法2
from classStudent import student #前面是模組名稱，後面是類別、變數或函數名稱
s2 = student("姚淳曜", 28, "0987654321")
s2.do_HW()