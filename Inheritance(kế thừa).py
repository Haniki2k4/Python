"""
__________________________________INTPUT____________________________________________________
"""
class Person:
  def __init__(self, fname, lname):
    #gán giá trị cho self.firstname và self.lastname
    self.firstname = fname 
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()

#tạo class con và kế thừa class Person
class Student(Person):
  pass #sử dụng nếu như không muốn thêm hoặc chỉnh sửa trong class con (giữ nguyên và chạy y như class Person)
  def __init__(self, fname, lname, year): #thêm hàm init vào student và không ảnh hưởng đến init của Person
    Person.__init__(self, fname, lname)
#Hoặc có thể sử dụng hàm sau để không phải gọi tên class cha(person): super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self): """thêm hàm in lời chào (không chạy trên Person vì person ko có hàm này)
                 (ví dụ về hàm thêm vào student nhưng vẫn giữ các hàm kế thừa khác của Person)"""
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome() #in ra welcome với các giá trị của x student

"""
_____________OUTPUT_____________________
John Doe
Mike Olsen
Welcome Mike Olsen to the class of 2019
________________________________________
"""

