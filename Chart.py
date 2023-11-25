#VẼ BIỂU ĐỒ
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
"""
'ĐƯỜNG'
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('Truc X')
plt.ylabel('Truc Y')
plt.title('Ham Sin trong khoang 0 den 3pi')
plt.legend(['Sin(x)','Cos(x)'])
plt.show()
"""


"""
'KIÊU ĐƯỜNG, MÀU'
x = np.arange(0., 5., 0.2)
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
plt.show()
"""

"""
'CỘT'
D = { 'KHDL':32,
     'KTPHCN':143,
     'KTXNYH':232,
     'YTCC':355,
     'KTMT':12,}
plt.bar(range(len(D)),D.values(), align='center')
plt.xticks(range(len(D)), D.keys())
plt.tile('HUPH')
plt,show
"""

"""
'CỘT GHÉP'
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Năm học 2021-2022", color= 'c')
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Năm học 2022-2023", color='b')
plt.legend()
plt.xlabel('Ngành')
plt.ylabel('Điểm trung bình')
plt.title('Ghép 2 biểu đồ')
plt.show()
"""

"""
import matplotlib.pyplot as plt
D = { 'KHDL': 32,
'KTPHCN': 310,
'KTXNYH': 360,
'YTCC': 580,
'CNDD': 340,
'CNKTMT': 29 }

plt.pie(D.values(), labels=D.keys(), autopct='%1.1f%%')
plt.axis('equal') # trục x = trục y
plt.show()
"""



labels = 'KHDL','KTPHCN','CNKTMT','KTXNYH','YTCC','CNDD'
sizes = [32,310,29,360,580,340]
explode = (0.1, 0, 0.1, 0, 0.04 5, 0)
figi, axl = plt.subplots()

axl.pie(sizes, explode = explode, labels=labels, autopct='%1.1f%%',shadow = True, startangle=90)
axl.axis('equal') # trục x = trục y
plt.show()


