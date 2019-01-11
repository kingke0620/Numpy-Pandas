import pandas as pd
import numpy as np

# #concatenating
# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
#
# print(df1)
# print(df2)
# print(df3)
# print('--------------')
#
# res = pd.concat([df1,df2,df3],axis=0)
# #这里仅是单纯的堆砌，还要更改索引变为连续的
# res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#忽略原来的索引
# print(res)




# #join,['inner','outer']
# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
# print(df1)
# print(df2)
# print('--------------')
# res = pd.concat([df1,df2],join='outer')#求并集，组合，有的字段数据缺失则用nan补
# res = pd.concat([df1,df2],join='inner',ignore_index=True)#求交集，组合
# print(res)




# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
# res = pd.concat([df1,df2],axis=1)#单纯合并，不考虑index
# res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])#按照df1的index进行合并
#
# print(df1)
# print(df2)
# print('----------------------')
# print(res)


#append
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
df3 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res = df1.append([df2,df3],ignore_index=True)#把df2,df3的数据加到df1上去

s1 = pd.Series([1,2.,3,4],index=['a','b','c','d'])
res1 = df1.append(s1,ignore_index=True)

print(df1)
print(df2)
print('----------------------')
print(res)
print(res1)