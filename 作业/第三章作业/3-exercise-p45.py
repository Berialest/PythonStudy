# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:15:46 2020

@author: user
"""

from pandas import DataFrame 
import numpy as np
data=[[np.random.randint(10,100) for j in range(1,8)]for i in range(1,51)]
print(data)
x=DataFrame(data,columns=['a','b','c','d','e','f','g'])
print(x)
x.to_csv('c:\\data\\3-exercise-45.csv',mode='w')