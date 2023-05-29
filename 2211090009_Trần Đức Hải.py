#Trần Đức Hải_2211090009
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""1."""
df = pd.read_csv('D:/haii/nguoi.csv')
print(df)

"""2."""
x = np.linspace(0, 5*np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title('Đồ thị hàm y=sin(x) và y=cos(x)')
plt.legend()
plt.show()

"""3."""
D = {'KHDL': 31,'KTXN': 140,'YTCC': 145,'PHCN': 55,'KTMT': 25}
explode = (0.025,0.025,0.025,0.025,0.025)
plt.pie(D.values(), labels=D.keys(),shadow=True, autopct='%1.1f%%', explode = explode)
plt.axis('equal') 
plt.suptitle('Số lượng sinh viên theo ngành của HUPH')
plt.show()


"""4."""
D = {'KHDL': 31,'KTXN': 140,'YTCC': 145,'PHCN': 55,'KTMT': 25}
colors = ['cyan','yellow','lightgreen','red','pink']
plt.bar(range(len(D)),D.values(), align='center', color= colors)
plt.xticks(range(len(D)), D.keys())
plt.title('Số lượng sinh viên theo ngành của HUPH')
plt.show()


