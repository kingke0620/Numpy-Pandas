import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

print(a,b)
c = a-b#a逐个减去b
c = b**2#**是python中的次方符号
c = 10*np.sin(a)
print(c)


#矩阵运算
d = np.array([[1,1],[0,1]])
e = np.arange(4).reshape((2,2))
f = d*e#对应位置的点乘
f_dot = np.dot(d,e)#矩阵乘法，dot->内积
#f_dot = d.dot(e)
print(d)
print(e)
print("不同的运算过程：")
print(f)
print(f_dot)

g = np.random.random((2,4))#随机0~1，给定行列
#np.sum(g) 等于 g.sum()
#np.min/max也一样
print(np.sum(g,axis=1))#axis为0表示在行数间求和，1表示在列数间求和