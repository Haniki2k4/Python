"""
__________________________________INTPUT____________________________________________________
Để có thể chạy mà không có lỗi thì nên xóa những phần comment """comment""" và #comment

List là một bộ sưu tập được sắp xếp trình tự và có thể thay đổi. Cho phép các thành viên trùng lặp.
"""
#Các kiểu dữ liệu chuỗi, int và boolean:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#Danh sách có chuỗi, số nguyên và giá trị boolean:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#Sử dụng list() để lập một danh sách:
thislist = list(("apple", "banana", "cherry")) # lưu ý cần 2 ngoặc tròn
print(thislist)

#In mục thứ hai trong danh sách fruits
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Thay đổi giá trị từ "apple" thành "kiwi", trong danh sách fruits.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits) 

#Sử dụng phương pháp nối (append) thêm để thêm "orange" vào danh sách fruits.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) 

#Sử dụng phương pháp chèn (insert) để thêm "lemon" làm mục thứ hai danh sách fruits.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits) 

#Sử dụng phương pháp xóa (remove) để loại bỏ "banana" khỏi danh sách fruits.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits) 

#Sử dụng lập chỉ mục phủ định (negative indexing) để in mục cuối cùng trong danh sách.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Sử dụng cú pháp (syntax) chính xác để in số mục trong danh sách.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Sử dụng một phạm vi danh mục để in mục thứ ba, thứ tư và thứ năm trong danh sách.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


"""
_____________OUTPUT_____________________
['apple', 'banana', 'cherry']
[1, 5, 7, 9, 3]
[True, False, False]
['abc', 34, True, 40, 'male']
['apple', 'banana', 'cherry']
banana
['kiwi', 'banana', 'cherry']
['apple', 'banana', 'cherry', 'orange']
['apple', 'lemon', 'banana', 'cherry']
['apple', 'cherry']
cherry
3
['cherry', 'orange', 'kiwi']
________________________________________
"""

