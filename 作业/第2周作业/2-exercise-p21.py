# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:27:27 2020

@author: user
"""

import numpy as np
import random
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])
print(subjects[0],subjects[1],subjects[3])
print( names[ (names== '方绮雯') ] )
print(names[ 1:-1 ])
print(subjects[1:3])
scores = np.array([[70,85,77,90,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])
print(scores[[1,3]])
print(scores[ [0,3]][:,[0,2] ])
print(scores[:,[0,4] ])
print( scores[(names == '王微') | (names == '刘旭阳')][:,(subjects == 'English') | (subjects == 'Art')] )
matrix=np.array([[random.randint(10, 19) for i in range(2)] for j in range(5)])
print(matrix)