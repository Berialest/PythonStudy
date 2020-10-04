# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:00:57 2020

@author: user
"""

import numpy as np
import random
shop = np.array(['大润发', '沃尔玛', '好德', '农工商'])
fruit = np.array(['苹果', '香蕉', '橘子', '芒果'])
price=np.array([[random.randint(4, 10) for i in range(4)] for j in range(4)])
print(price)
print(price[(0,2),(0,1)]+1)
print(price[3,:]-1)
print(price[:,fruit=="苹果"].mean())
print(price[:,fruit=="芒果"].mean())
print(shop[price[:,fruit=="橘子" ].argmax()])