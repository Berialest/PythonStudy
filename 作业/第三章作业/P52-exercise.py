# -*- coding: utf-8 -*-
"""
Created on Mon May 18 07:57:30 2020

@author: user
"""

import pandas as pd
import numpy as np
from pandas import DataFrame
data=pd.read_excel('c:\\data\\studentsInfo.xlsx','Group3')
print(data)
data1=data.loc[:,['序号','性别','年龄']]
print(data1)
data2=data.loc[:,['序号','身高','体重','成绩']]
print(data2)
data3=pd.merge(data1,data2,how='inner')
print(data3)
print(data3.sort_values(by='成绩',ascending=True))
data3['身高排名']=data3['身高'].rank(method='min',ascending=False)
print(data3)