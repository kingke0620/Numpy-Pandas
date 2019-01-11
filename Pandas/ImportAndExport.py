#可读取的格式：csv、excel、hdf、sql、json、msgpack、html、gbq、stata、sas、clipboard、pickle
import pandas as pd

data = pd.read_csv('ImportAndExport.csv')
print(data)#自动加上索引
data.to_pickle('ImportAndExport.pickle')#保存到pickle文件

#其余文件格式的语法与上相同