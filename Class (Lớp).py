#Tạo một lớp có tên MyClass, với thuộc tính có tên x:
print('(TEST CALSS PYTHON)')    
print('Tạo MyClass và nhập gtri của x=5 rồi sau đó in Gtri của x ra')
class MyClass:
  x = 5
  
#Tạo một đối tượng có tên p3 và in giá trị của x:
p3 = MyClass()
print(p3.x)
print('----------------------------------------------------')

"""
______________________________________________________________________________
"""


"""Tạo một lớp có tên Person
sử dụng hàm __init__() để gán giá trị Đối với tên và tuổi:
"""
class Person:
 def __init__(self, name, age, gender, race):
     """có thể sử dụng các từ như mysillyobject và abc thay vì self"""
     self.name = name
     self.age = age
     self.gender = gender
     self.race = race
#Chèn một hàm in lời chào và thực thi nó trên đối tượng p1:
 def myfunc(self):
    print("Hello my name is " + self.name +"," ,self.age, "tuổi")
#Biểu diễn chuỗi của một đối tượng VỚI hàm __str__():
 def __str__(self):
    return f"{self.name}({self.age}), {self.gender}, {self.race}"
p1 = Person("John", 36,"Women","Hispo")
p2 = Person("Kayle", 24,"Women","Hispo")
#Biểu diễn theo từng giá trị
print(p1.name)
print(p1.age)
print(p1.gender)
#Biểu diễn đưới dạng chuỗi
print(p1)
p1.myfunc()
p2.myfunc()
#Thay đổi thuộc tính: Đặt tuổi từ p1 thành 40:
p1.age = 40
print(p1.age)
p1.myfunc()

#Xóa thuộc tính age khỏi đối tượng p1:
del p1.age

#Xóa đối tượng p1:
del p1
