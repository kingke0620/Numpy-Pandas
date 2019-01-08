import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B))# vertical stack，上下合并
D = np.hstack((A,B))#horizontal stack，左右合并
'''
print(C)
print(D)
print(A.shape)#返回“3，”是因为shape返回tuple类型，单个元素情况下必须写逗号
print(C.shape)#两行三列
print(D.shape)
'''

'''把一个横向的列表变成纵向向量'''
#直接用A.T是不可行的
A = A [:,np.newaxis]#该操作表示增加一个维度，放在逗号前是横向增加，逗号后是纵向增加
print(A)#增加纵向维度后的A会变成纵向
print(A.shape)
print(A.reshape(A.size,1))
print(A.reshape(-1,1))
print(A[np.newaxis,:])
'''记住reshape不是普遍适用的，但是[:,np.newaxis]不管元素有多少个都可以使用'''
A = A.squeeze()#squeeze压缩维度为1的数组
print(A.shape)
print(A)

E = np.concatenate((A,A,B))#进行多个矩阵的合并
print(E)

#同时可以确认是在哪一个维度进行合并
E = np.concaternate((A,B,B,A),axis=0)#0代表纵向合并，操作列。1代表横向合并，操作行