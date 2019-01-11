import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

#plt data

# #1 Series线性数据
# data =pd.Series(np.random.randn(1000),index=np.arange(1000))
# data = data.cumsum()
# data.plot()
# #plt.plot(x=,y=)
# plt.show()

#2 DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()#对应column的累加值
print(data.head())#默认前五个
# data.plot()

'''
plot methods:
"bar、hist、box、kde、area、scatter、scatter、hexbin、pie"
'''

ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')#散点图
bx = data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)#ax=ax代表在同一个坐标系下
plt.show()


