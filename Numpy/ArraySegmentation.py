import numpy as np
A = np.arange(12).reshape(3,4)
print(A)

#横向分割
print(np.split(A,2,axis=1))#第二个参数表示分成几块，axis=1代表对行进行操作（横向，和Combination一样），分成两列
print(np.hsplit(A,2))
#纵向分割
print(np.split(A,3,axis=0))
print(np.vsplit(A,3))
# axis理解为对shape两个参数的索引，所以0和1代表不同的含义
#第二个参数使用整数是等分
