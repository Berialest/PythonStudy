# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:25:00 2020

@author: user
"""

import numpy as np
rndwlk = np.random.normal(0,1, size = (3,10))
print(rndwlk)
position = rndwlk.cumsum(axis = 1)
print(position)
dists = np.sqrt(position[0]**2+position[1]**2+position[2]**2)
print(dists)
zmax = abs(position[2].max())
fmax = abs(position[2].min())
if zmax > fmax:
    print(zmax)
else:
    print(fmax)
print(dists.min())