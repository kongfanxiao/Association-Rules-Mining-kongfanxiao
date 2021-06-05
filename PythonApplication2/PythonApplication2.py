import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import category_encoders as ce
import csv
import codecs
import os
import itertools
Winery = ["Testarossa","Chehalem","Naggiar","Milbrandt","Cayuse","Maryhill","Gorman"]
os.getcwd() #获取当前工作路径
datawine1 = pd.read_csv('D:/1007storage/visual_studio/Python/data/winemag-data-130k-v2.csv/winemag.csv') #读取数据 
datawine2 = datawine1.dropna(axis = 0)  #删除包括nan的行

datawine = datawine2[['variety','winery']]
print('0000000000')
winery_count = datawine['winery'].value_counts()
print(winery_count[9:20])

#for temp in Winery: #按照winery对variety进行分类    
#    temp_data = datawine[datawine['winery'].isin(Winery)]
#    exec("Winery%s = temp_data"%temp)


datawine123 = datawine.groupby(datawine['winery'])

i = 0
for temp in Winery:
    
    w = 2 * i
    #dfName = "Winery" + str(temp)
    print('---------------分隔符---------------',i,"  ",temp)
    i = i +1
    filepath = "D:/1007storage/visual_studio/Python/Association-Rule-Mining-python3/data/txt2/points-variety"+str(i)+".txt"
    #dfData = eval(dfName)
    dfData1 = datawine123.get_group(temp)['variety']
    dfData2 = dfData1.unique()
    dfData3 = pd.DataFrame(dfData2)
    
    print(datawine123.get_group(temp))
    #dfData3.to_excel(filepath,sheet_name=sheetname,startcol=w,index=False) #写入xlsx
    dfData3.to_csv(filepath,index=False,sep=' ')