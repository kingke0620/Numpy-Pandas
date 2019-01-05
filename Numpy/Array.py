import numpy as np
a = np.array([2,3,4],dtype=np.int)#最后一个参数决定array中的参数形式，int32/float16诸如此类
print(a.dtype)#打印出的格式跟随python版本，自己默认32位
b = np.zeros((3,4))#3行4列零矩阵
c = np.ones((3,4),dtype=np.int16)
d = np.empty((3,4))#几乎接近于0，因为empty不初始化分配给d的内存

#数列
e = np.arange(10,20,2)#10到20的数列，步长2
f = np.arange(12).reshape((3,4))#3行4列的0~11的数列
g = np.linspace(1,10,5)#1~10的5等分数列