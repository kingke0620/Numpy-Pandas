import numpy as np
import pandas as pd

dates = pd.date_range('20190109',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

#axis如果搞混，去引.txt中看一下
#0表示纵轴，变化是纵向的。1表示横轴，变化是横向的
#丢弃数据(注意函数都是没有写全的)
print(df.dropna(axis=0,how='any'))#how={'any','all'};all:只有在这一行所有的数据都是nan的时候才会丢弃
print(df.fillna(value=0))#对nan值的填充
#.isnull()如果确实有丢失，返回的是True
print(np.any(df.isnull())==True)#检查是否数值缺失,
