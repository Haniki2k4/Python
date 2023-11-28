"""__________________________________INTPUT____________________________________________________

Dict là một bộ sưu tập đượcsắp xếp trình tự và có thể thay đổi. Không có thành viên trùng lặp.
"""

#Tạo và in từ điển (dictionary):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#In giá trị "brand" của từ điển:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#In số lượng mục trong dictionary:
print(len(thisdict))

#Các giá trị trong dictionary có thể thuộc bất kỳ kiểu dữ liệu nào:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#Sử dụng phương thức dict() để tạo từ điển:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Sử dụng phương thức get để in giá trị của khóa "model" của car dictionary.
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Đổi gái trị của "year" từ 1964 thành 2020
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)

#Thêm cặp khóa/giá trị "color" : "red" vào car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)

#Sử dụng phương thức pop để xóa "model" khỏi car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#Sử dụng phương thức clear để làm sạch car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

"""
_____________OUTPUT_____________________
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Ford
3
{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}
{'name': 'John', 'age': 36, 'country': 'Norway'}
Mustang
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
{'brand': 'Ford', 'year': 1964}
{}
________________________________________
"""

