import numpy as np

A = np.arange(3,15)
print(A)
print(A[3])#一维输出第几个

B = np.arange(3,15).reshape((3,4))
print(B)
print(B[2])#二维输出第几行
print(B[1][0])
print(B[1,0])
print(B[1,:])#：一般代表所有的

print('迭代输出开始')
print('迭代行')
for row in A:
    print(row)
#分别迭代行列
print('迭代列')
for column in A.T:
    print(column)

print('输出所有元素')
print(A.flatten())#数组变列表，“铺平”
for item in A.flat:
    print(item)#将数组内每一个元素输出