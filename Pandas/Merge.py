import pandas as pd
'''这里分了几个模块，运行那个模块直接揭开注释即可'''
#merging two dataframe by key/key.(may be used in database)
#1 simple example
# left = pd.DataFrame({'key':['K0','K1','K2','K3'],
#                      'A':['A0','A1','A2','A3'],
#                      'B':['B0','B1','B2','B3']})
# right = pd.DataFrame({'key':['K0','K1','K2','K3'],
#                      'C':['C0','C1','C2','C3'],
#                      'D':['D0','D1','D2','D3']})
#
# print(left)
# print(right)
#
# res = pd.merge(left,right,on='key')#基于'key'column进行合并
# print(res)

# #2 consider two keys
# left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
#                      'key2':['K0','K1','K0','K1'],
#                      'A':['A0','A1','A2','A3'],
#                      'B':['B0','B1','B2','B3']})
# right = pd.DataFrame({'key1':['K0','K1','K1','K2'],
#                       'key2':['K0','K0','K0','K0'],
#                      'C':['C0','C1','C2','C3'],
#                      'D':['D0','D1','D2','D3']})
#
# print(left)
# print(right)
# res = pd.merge(left,right,on=['key1','key2'])#默认inner，只考虑相同的key（先做笛卡尔积，再选取出key相同的值进行组合）
# #how = ['left','right','inner','outer']
# res1 = pd.merge(left,right,on=['key1','key2'],how='outer')#不管key是否相同，都复制下来，缺失的值nan填充(联想数据库的链接操作)
# print(res)
# print(res1)

# #3 indicator
# df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
# df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# print(df1)
# print(df2)
# res = pd.merge(df1,df2,on='col1',how='outer',indicator=True)#表明合并的样式（left_only仅左侧有数据）
# res1 = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')#修改字段，indicator默认是False
# print(res)
# print(res1)

# #4 merge by index
# left = pd.DataFrame({'A':['A0','A1','A2','A3'],
#                      'B':['B0','B1','B2','B3']},
#                     index=['K0','K1','K2','K3'])
# right = pd.DataFrame({'C':['C0','C1','C2'],
#                      'D':['D0','D1','D2']},
#                      index=['K0','K1','K2'])
# print(left)
# print(right)
# print('------------------------')
# #left_index and right_index
# #第三第四个参数，表明先考虑的是index
# res = pd.merge(left,right,left_index=True,right_index=True,how='outer')
# res1 = pd.merge(left,right,left_index=True,right_index=True,how='inner')
#
# print(res)
# print(res1)

# #5 handle overlapping
# boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
# girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
# print(boys)
# print(girls)
# #假设情形：这里是两个表，男生女生，因为age字段一样，在使用inner方式连接时会丢失数据
# #因此进行修改,以区分名字相同，意义不同的数据(suffix意为后缀)
# res = pd.merge(boys,girls,on='k',how='inner')
# res1 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
# print(res)
# print(res1)

#concat默认是'outer',merge默认是'inner'
#学完了记得分析concat与merge的区别