# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:38:50 2020

@author: user
"""

import numpy as np
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])
scores = np.array([[70,85,77,90,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])
print(scores[:,subjects=='English']-3)
for i in names:
    print(i,end='')
    print('的平均成绩是:',scores[names==i].mean())
a=np.random.uniform(-1,1,size=(3,4))
print(a.sum())