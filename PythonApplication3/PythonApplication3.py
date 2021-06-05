import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import category_encoders as ce
import csv
import codecs
import os
from apyori import apriori
dataset = pd.read_csv(('D:/1007storage/visual_studio/Python/data/winemag-data-130k-v2.csv/winemag.csv'), usecols=['winery'])
def create_dataset(data):
    for index, row in data.iterrows():
        data.loc[index, 'winery'] = row['winery'].strip()
    data = data['winery'].str.split(" ", expand = True)
    # 按照list来存储
    output = []
    for i in range(data.shape[0]):
        output.append([str(data.values[i, j]) for j in range(data.shape[1])])
    return output

dataset = create_dataset(dataset)
association_rules = apriori(dataset, min_support = 0.05, min_confidence = 0.7, min_lift = 1.2, min_length = 2)
association_result = list(association_rules)
association_result
