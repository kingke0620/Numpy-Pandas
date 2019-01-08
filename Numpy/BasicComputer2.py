import numpy as np
A = np.arange(2,14).reshape((3,4))

print(A)
print(np.argmin(A))#并非输出值，而是输出所在的索引
print(np.argmax(A))
print(A.mean())#数列的平均值(把模块看做对象)
print(np.mean(A,axis=0))#0代表对列进行计算，1代表对行进行运算
print(np.average(A))#数列的平均值(把数据看做对象)
print(np.median(A))#中位数
print(np.cumsum(A))#前n项和
print(np.diff(A))#每两项之间的差
print(np.transpose(A))#转置矩阵
print((A.T).dot(A))#转置后矩阵乘法
#注意！".T"表示的transport只对矩阵有效，不能把一个序列转之后成为矩阵
print(np.clip(A,5,9))#所有大于9的变为9，小于5的变为5，区间内的值不变






