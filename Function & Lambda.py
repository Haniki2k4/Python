
'''
------------FUNCTION---------------
'''

#Nếu bạn không biết số lượng đối số sẽ được truyền vào hàm của bạn, thêm tiền tố * vào định nghĩa hàm
def my_function(*kids):
  print("The youngest child is " + kids[2])

#Nếu bạn không biết số lượng đối số từ khóa sẽ được chuyển vào hàm của bạn, thêm tiền tố ** vào định nghĩa hàm
def my_function(**kid):
  print("His last name is " + kid["lname"])

#một hàm với một đối số (fname). Khi hàm được gọi, chúng tôi chuyển một tên, được sử dụng bên trong hàm để in tên đầy đủ:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

'''
------------LAMBDA---------------
'''
#Thêm 10 vào đối số , và Trả kết quả:a
x = lambda a : a + 10
print(x(5))

#Nhân đối số với đối số và trả về kết quả:a,b
x = lambda a, b : a * b
print(x(5, 6))

#Tổng đối số ,, và trả về:abc
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


