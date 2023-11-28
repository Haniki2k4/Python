'''
------------MODULE--------------


Để tạo một mô-đun, chỉ cần lưu mã bạn muốn trong một tệp có phần mở rộng tệp:.py
'''


#Ví dụ: lưu mã này trong tệp có tên mymodule.py
def greeting(name):
  print("Hello, " + name)

  #Sử dụng mô-đun mà chúng ta vừa tạo, bằng cách sử dụng câu lệnh:import
  #Nhập mô-đun có tên mymodule và gọi hàm lời chào:
import mymodule
mymodule.greeting("Jonathan")

#Mô-đun có thể chứa các hàm và các biến của Tất cả các loại (mảng, từ điển, đối tượng, v.v.):
  #Ví dụ: Lưu mã này trong tệp mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
  #Ví dụ: Nhập mô-đun có tên mymodule và truy cập từ điển person1:
import mymodule
a = mymodule.person1["age"]
print(a)

#Cú pháp để nhập mô-đun có tên "mymodule"
import mymodule

#Nếu bạn muốn tham chiếu đến một mô-đun bằng cách sử dụng một tên khác, bạn có thể tạo bí danh cho mô-đun
import mymodule as mx

#In tất cả các biến và tên hàm của mô-đun "mymodule"
import mymodule
print(dir(mymodule))

#Mô-đun được đặt tên có một chức năng và một từ điển:mymodule
def greeting(name):
  print("Hello, " + name)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
  #Nhập từ điển person1 của mô-đun "mymodule" 
from mymodule import person1
print (person1["age"])
