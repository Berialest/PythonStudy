# -*- coding: utf-8 -*-
"""
Created on Mon May 18 07:21:07 2020

@author: user
"""

import pandas as pd
import numpy as np
from pandas import DataFrame
stu=pd.read_excel('c:\\data\\studentsInfo.xlsx','Group1',index_col=0)
print(stu)
stu['案例教学']=np.nan
print(stu)
stu1=stu.dropna(thresh=7)
print(stu1)
stu2=stu.dropna(axis=1,how='all')
print(stu2)
stu3=stu2.fillna({'体重':stu2['体重'].mean(),'成绩':stu2['成绩'].mean()})
print(stu3)
stu4=stu3.fillna(method='ffill')
print(stu4)
print(stu4.fillna({'月生活费':stu4['月生活费'].median()}))