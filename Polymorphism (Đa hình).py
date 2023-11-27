"""
__________________________________INTPUT____________________________________________________
"""


"""
Polymorphism (Đa hình)
-đề cập đến phương thức / chức năng / toán tử có cùng tên có thể được thực thi trên nhiều đối tượng hoặc lớp học.
"""
#string
x = "Hello World!"
print(len(x))

#tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

#dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
"""
_____________OUTPUT_____________________
12
3
3
________________________________________
"""


"""
Class Polymorphism (Đa hình lớp):
-thường được sử dụng trong các phương thức Class, nơi chúng ta có thể có nhiều các lớp có cùng tên phương thức.
"""

class Vehicle:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def move(self):
    print("Move!")
    
  def func(self):
  	print("Production year: ", self.year)

  def __str__(self):
   return f"Information: {self.brand} {self.model} ({self.year})"
 
class Car(Vehicle):
  pass #kế thừa tất cả các methods của class Vehicle

class Boat(Vehicle):
  def move(self): #ghi đè lên phương thức move của Vehicle
    print("Relief: River, Sea")

class Plane(Vehicle):
  def move(self): #ghi đè lên phương thức move của Vehicle 
    print("Relief: Sky")

car1 = Car("Ford", "Mustang", 2020) #Tạo 1 đối tượng (object) Car
boat1 = Boat("Ibiza", "Touring 20", 2023) #Tạo 1 đối tượng (object) Boat
plane1 = Plane("Boeing", "747", 2019) #Tạo 1 đối tượng (object) Plane

#Dùng vòng for thực hiện cùng một phương thức cho cả ba lớp.
for x in (car1, boat1, plane1):
  print(x.brand, x.model)
  x.move()
  x.func()
  print(x)
  print('__________')


"""
_____________OUTPUT_____________________
Ford Mustang
Move!
Production year:  2020
Information: Ford Mustang (2020)
__________
Ibiza Touring 20
Relief: River, Sea
Production year:  2023
Information: Ibiza Touring 20 (2023)
__________
Boeing 747
Relief: Sky
Production year:  2019
Information: Boeing 747 (2019)
__________
________________________________________
"""
