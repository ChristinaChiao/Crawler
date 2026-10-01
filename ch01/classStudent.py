class student():
  def __init__(self, name, age, tel): #屬性初始化：姓名、年齡、電話
    self.name = name #self代表"物件"本身，name是屬性名稱
    self.age = age
    self.tel = tel
  def take_exam(self):
    print(self.name, "參加考試")
  
  def do_HW(self):
    print(self.name, "寫作業")
    
# s1 = student("李國毅", 35, "0912345678")
# s2 = student("姚淳曜", 28, "0987654321")
# print(s1.name, s1.age, s1.tel)
# print(s2.name, s2.age, s2.tel)

# s1.take_exam() #s1物件.take_exam()方法
# s2.do_HW()