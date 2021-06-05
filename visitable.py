import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import category_encoders as ce
import csv
import codecs
import os
import itertools

df = pd.read_csv('D:/1007studying/2021/datamining/work/associate-rule-mining/results/results.csv') #读取数据 
#print(datawine1)
support_X = df['Support Of X']
support_XY = df['Support of XY']

df1 = pd.read_csv('D:/1007studying/2021/datamining/work/associate-rule-mining/results/results_not_used.csv') #读取数据
support_X1 = df1['Support Of X']
support_XY1 = df1['Support of XY']

#print(support_XY)
def histpic(nums1,nums2,nums3,nums4,d,histname):               #绘制直方图
    fig,axes = plt.subplots(nrows=2,ncols=2)
    plt.suptitle(histname,color = 'red')
    axes[0,0].set(title='results support_X')
    axes[0,1].set(title='results support_XY')
    axes[1,0].set(title='results support_X notused')
    axes[1,1].set(title='results support_XY notused')
    numbins1 = 14
    numbins2 = 1
    numbins3 = 1
    numbins4 = 1
    axes[0,0].hist(nums1,numbins1)				#绘制直方图
    axes[0,1].hist(nums2,numbins2)
    axes[1,0].hist(nums3,numbins3)
    axes[1,1].hist(nums4,numbins4)
    axes[0,0].grid()                            #网格
    axes[0,1].grid()
    axes[1,0].grid()
    axes[1,1].grid()
    plt.show()
    return 1
def fiveNumber(nums):#五数概括 Minimum（最小值）、Q1、Med-ian（中位数、）、Q3、Maximum（最大值）
	Minimum=min(nums)
	Maximum=max(nums)
	Q1=np.percentile(nums,25)
	Median=np.median(nums)
	Q3=np.percentile(nums,75)
	IQR=Q3-Q1
	lower_limit=Q1-1.5*IQR #下限值
	upper_limit=Q3+1.5*IQR #上限值
	print("Minimum,Q1,Median,Q3,Maximum")
	return Minimum,Q1,Median,Q3,Maximum
#plt.suptitle("support_hist",color = 'red')
#plt.histpic(winepoints,num_bins)	
print("----------------------------------------------------------")
print(fiveNumber(support_X))
print("----------------------------------------------------------")
print(fiveNumber(support_XY))
print("----------------------------------------------------------")
print(histpic(support_X,support_XY,support_X1,support_XY1,50,"support_hist"))   #绘制直方图

