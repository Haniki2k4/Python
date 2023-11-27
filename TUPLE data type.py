"""
__________________________________INTPUT____________________________________________________
Để có thể chạy mà không có lỗi thì nên xóa những phần comment """comment""" và #comment

Tuple là một bộ sưu tập được sắp xếp trình tự và không thể thay đổi. Cho phép các thành viên trùng lặp.
"""

#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
#Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
#Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
#Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


"""
_____________OUTPUT_____________________
apple
Yes, apple is a fruit!
{'orange', 'banana', 'apple', 'cherry'}
{'grapes', 'mango', 'orange', 'apple', 'cherry', 'banana'}
{'apple', 'cherry'}
{'apple', 'cherry'}
________________________________________
"""
