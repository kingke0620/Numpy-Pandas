import numpy as np
import pandas as pd

dates = pd.date_range('20190109',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2] = 1111#单值修改
df.loc['20190112','B'] = 2222#如果表中没有这个行的字段，则会自动创建出一条新数据
df[df.A>4] = 0#这里的改动是针对选择的数据所在列的整体改动，并不是仅一个字段
df.A[df.A<4] = 1#这样是仅对A列的数据进行改动
df['F'] = np.nan#新加一列全为null值
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20190109',periods=6))#这里新加了一列，数据为列表1~6，index规定其所对应的数据，对应好才能新增上去

print(df)
