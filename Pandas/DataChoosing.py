import numpy as np
import pandas as pd

dates = pd.date_range('20190109',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print('-------------')
print(df['A'],df.A)#简单选择行列
print(df[0:3],df['20190110':'20190112'])#简单选择行列
print('--------------')

'''这里很重要，是使用iloc和loc进行的精确定位'''
print(df.loc['20190109'])#以标签，具体地选择
print(df.loc[:,['A','B']])#选择了AB列
print(df.loc['20190109',['A','B']])#选择了AB列,20190109行
print('--------------')
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])#这里进行了一个切片，输出第三第四行，第一第二列（从零开始）
print(df.iloc[[1,3,5],1:3])#不连续的单个筛选
print('--------------')
print(df.ix[:3,['A','C']])#这里是混合了两种筛选方式
#注意ix在python3中已被弃用

print('--------------')
#Bolean indexing
print(df)
print(df[df.A>8])#有额外的筛选条件直接在后面跟上[df.*>*]即可