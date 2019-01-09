import pandas as pd
import numpy as np

# s = pd.Series([1,3,6,np.nan,44,1])#nan:not a number
# print(s)
print('-----------------------------')
dates = pd.date_range('20190101',periods = 6)
print(dates)
print('-----------------------------')
#这里DataFrame第一个参数就是numpy的数据，行的索引是dates，列的索引是columns
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','bc','d'])
print(df)
print('-----------------------------')
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))#默认使用0~n作为行列索引
print(df1)
print('-----------------------------')
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20190109'),
                    'C':np.array([3]*4,dtype='int32')})#以字典作为参数，输出呀一个表格
print(df2)
print(df2.dtypes)#打印所有维度上数据的属性
print(df2.index)#打印所有的行索引
print(df2.columns)#打印所有的列索引
print(df2.values)#按行输出所有值
print(df2.describe())#数据帧描述，对矩阵内的数字进行常用运算（count，min，max等等）
print(df2.sort_index(axis=1,ascending=False))
#ascending决定顺序逆序排列，axis=0代表纵向排序，axis=1代表横向排序
print(df2.sort_values(by='A'))#根据单行值进行排序
