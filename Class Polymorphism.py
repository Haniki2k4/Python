"""
__________________________________INTPUT____________________________________________________
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
  pass

class Boat(Vehicle):
  def move(self): #ghi đè lên phương thức move của Vehicle
    print("Relief: River, Sea")

class Plane(Vehicle):
  def move(self):
    print("Relief: Sky")

car1 = Car("Ford", "Mustang", 2020) #Create a Car object
boat1 = Boat("Ibiza", "Touring 20", 2023) #Create a Boat object
plane1 = Plane("Boeing", "747", 2019) #Create a Plane object

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
