import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import category_encoders as ce
import csv
import codecs
import os
import itertools

os.getcwd() #获取当前工作路径
datawine1 = pd.read_csv('D:/1007storage/visual_studio/Python/data/winemag-data-130k-v2.csv/winemag.csv') #读取数据 
datawine2 = datawine1.dropna(axis = 0)  #删除包括nan的行
datawine = datawine2[['variety','points']]
print('0000000000')
wine_points = datawine['points'].unique()   #80-100
def generateC1(dataSet):#生成初始候选集
    productDict = {}
    returneSet = []
    for data in dataSet:
        for product in data:
            if product not in productDict:
               productDict[product] = 1
            else:
                 productDict[product] = productDict[product] + 1
    for key in productDict:
        tempArray = []
        tempArray.append(key)
        returneSet.append(tempArray)
        returneSet.append(productDict[key])
        tempArray = []
    return returneSet
#通过将候选集作为输入来创建Frequent项集
def generateFrequentItemSet(CandidateList, noOfTransactions, minimumSupport, dataSet, fatherFrequentArray):
    frequentItemsArray = []
    for i in range(len(CandidateList)):
        if i%2 != 0:
            support = (CandidateList[i] * 1.0 / noOfTransactions) * 100
            if support >= minimumSupport:
                frequentItemsArray.append(CandidateList[i-1])
                frequentItemsArray.append(CandidateList[i])
            else:
                eleminatedItemsArray.append(CandidateList[i-1])

    for k in frequentItemsArray:
        fatherFrequentArray.append(k)

    if len(frequentItemsArray) == 2 or len(frequentItemsArray) == 0:
        returnArray = fatherFrequentArray
        return returnArray

    else:
        generateCandidateSets(dataSet, eleminatedItemsArray, frequentItemsArray, noOfTransactions, minimumSupport)
    #print(groupby_winery.max().shape[0])
    #print(wine_winery_designation2)
def generateCandidateSets(dataSet, eleminatedItemsArray, frequentItemsArray, noOfTransactions, minimumSupport):
    onlyElements = []
    arrayAfterCombinations = []
    candidateSetArray = []
    for i in range(len(frequentItemsArray)):
        if i%2 == 0:
            onlyElements.append(frequentItemsArray[i])
    for item in onlyElements:
        tempCombinationArray = []
        k = onlyElements.index(item)
        for i in range(k + 1, len(onlyElements)):
            for j in item:
                if j not in tempCombinationArray:
                    tempCombinationArray.append(j)
            for m in onlyElements[i]:
                if m not in tempCombinationArray:
                    tempCombinationArray.append(m)
            arrayAfterCombinations.append(tempCombinationArray)
            tempCombinationArray = []
    sortedCombinationArray = []
    uniqueCombinationArray = []
    for i in arrayAfterCombinations:
        sortedCombinationArray.append(sorted(i))
    for i in sortedCombinationArray:
        if i not in uniqueCombinationArray:
            uniqueCombinationArray.append(i)
    arrayAfterCombinations = uniqueCombinationArray
    for item in arrayAfterCombinations:
        count = 0
        for transaction in dataSet:
            if set(item).issubset(set(transaction)):
                count = count + 1
        if count != 0:
            candidateSetArray.append(item)
            candidateSetArray.append(count)
    generateFrequentItemSet(candidateSetArray, noOfTransactions, minimumSupport, dataSet, fatherFrequentArray)

    #wine_points_designation = wine_points_designation2.sort_values("points")    #按照points列进行排序
    #print(wine_points_designation)  #输出排序后的结果
    #df = df1.city.value_counts()  
    #print(df2)
    
def generateAssociationRule(freqSet):#该函数以所有频繁集为输入，生成关联规则
    associationRule = []
    for item in freqSet:
        if isinstance(item, list):
            if len(item) != 0:
                length = len(item) - 1
                while length > 0:
                    combinations = list(itertools.combinations(item, length))
                    temp = []
                    LHS = []
                    for RHS in combinations:
                        LHS = set(item) - set(RHS)
                        temp.append(list(LHS))
                        temp.append(list(RHS))
                        #print(temp)
                        associationRule.append(temp)
                        temp = []
                    length = length - 1
    return associationRule

def aprioriOutput(rules, dataSet, minimumSupport, minimumConfidence):#以关联规则作为输入来创建算法的最终输出
    returnAprioriOutput = []
    for rule in rules:
        supportOfX = 0
        supportOfXinPercentage = 0
        supportOfXandY = 0
        supportOfXandYinPercentage = 0
        for transaction in dataSet:
            if set(rule[0]).issubset(set(transaction)):
                supportOfX = supportOfX + 1
            if set(rule[0] + rule[1]).issubset(set(transaction)):
                supportOfXandY = supportOfXandY + 1
        supportOfXinPercentage = (supportOfX * 1.0 / noOfTransactions) * 100
        supportOfXandYinPercentage = (supportOfXandY * 1.0 / noOfTransactions) * 100
        confidence = (supportOfXandYinPercentage / supportOfXinPercentage) * 100
        if confidence >= minimumConfidence:
            supportOfXAppendString = "Support Of X: " + str(round(supportOfXinPercentage, 2))
            supportOfXandYAppendString = "Support of X & Y: " + str(round(supportOfXandYinPercentage))
            confidenceAppendString = "Confidence: " + str(round(confidence))

            returnAprioriOutput.append(supportOfXAppendString)
            returnAprioriOutput.append(supportOfXandYAppendString)
            returnAprioriOutput.append(confidenceAppendString)
            returnAprioriOutput.append(rule)

    return returnAprioriOutput

print('---------------分隔符---------------')
for temp_points in wine_points: #按照points对variety进行分类    从80-100
    temp_data = datawine[datawine['points'].isin([temp_points])]
    exec("points%s = temp_data"%temp_points)
for temp_points in wine_points:
    i = temp_points - 80
    w = 2 * i
    dfName = "points" + str(temp_points)
    sheetname = "data" + str(w)
    filepath = "D:/1007storage/visual_studio/Python/Association-Rule-Mining-python3/data/txt/points-variety"+str(i)+".txt"
    dfData = eval(dfName)
    dfData1 = dfData['variety']
    dfData2 = dfData1.unique()
    dfData3 = pd.DataFrame(dfData2)
    print('---------------分隔符---------------',i)
    #dfData3.to_excel(filepath,sheet_name=sheetname,startcol=w,index=False) #写入xlsx
    dfData3.to_csv(filepath,index=False,sep=',')


minimumSupport = input('Enter minimum Support: ')
minimumConfidence = input('Enter minimum Confidence: ')
minimumSupport = int(minimumSupport)
minimumConfidence = int(minimumConfidence)
nonFrequentSets = []
allFrequentItemSets = []
tempFrequentItemSets = []
dataSet = []
eleminatedItemsArray = []
noOfTransactions = 0
fatherFrequentArray = []
something = 0
with open("D:/1007storage/visual_studio/Python/Association-Rule-Mining-python3/data/txt2/text.txt",'r') as fp:
    lines = fp.readlines()

for line in lines:
    line = line.rstrip()
    dataSet.append(line.split(","))

noOfTransactions = len(dataSet)
firstCandidateSet = generateC1(dataSet)
frequentItemSet = generateFrequentItemSet(firstCandidateSet, noOfTransactions, minimumSupport, dataSet, fatherFrequentArray)
associationRules = generateAssociationRule(fatherFrequentArray)
AprioriOutput = aprioriOutput(associationRules, dataSet, minimumSupport, minimumConfidence)

i123 = 1
if len(AprioriOutput) == 0:
    print("There are no association rules for this support and confidence.")
else:
    for i in AprioriOutput:
        if i123 == 4:
            print(str(i[0]) + "------>" + str(i[1]))
            i123 = 0
        else:
            print(i, end='  ')
        i123 = i123 + 1






