'''
numpy是基于矩阵的计算
'''
import numpy as np

#列表转换为矩阵
array = np.array([[1,2,3],[2,3,4]])
print(array)
print('number of dimension',array.ndim)
print('shape',array.shape)#行列数
print('size',array.size)#有多少元素