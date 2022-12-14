#画图的基本命令
import matplotlib.pyplot as plt
import numpy as np

import os
os.chdir('C:\\Users\\wiki\\Desktop\\bigpassage\\JavaScript')#更改路径，''里面为更改的路径

f = open("data.js")
data = []
scale = 0
strip_no = ""
for num,line in enumerate(f):
    if(num == 0):
        js = line.strip()
        js_list = js.split("[")
        js = js_list[1].split("]")[0]
        data = js.split(',')
        data = list(map(float, data))  # 把list内的元素变成float型
    elif(num == 1):
        scale = float(line)
    elif(num == 2):
        strip_no = line.replace("\n","")

x=np.linspace(0,len(data),len(data))
y=data
plt.plot(x,y,lw=2,c='blue',label='thick')
plt.legend(strip_no)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
# plt.xlim(0,len(data))
plt.ylim(max(max(data)+0.05,scale + 0.05),min(min(data)-0.05,scale -0.05))
plt.grid(ls=":",c='b',)#打开坐标网格
# plt.title("y=sin(x)")
plt.axhline(y=scale-0.1,c="red")#添加水平直线
plt.axhline(y=scale+0.1,c="red")#添加水平直线
# plt.axvline(x=4,ls="-",c="green")#添加垂直直线
plt.savefig(strip_no)

