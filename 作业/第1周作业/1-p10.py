# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:42:49 2020

@author: user
"""

print(3+5==6)
course='Python Programming'
score=92.5
print(course+": "+str(score))
t=('Lucy',('Math',90))
print(t)
t[1][1]
ls=[]
ls.append(1)
ls.append('wang')
print(ls)
ls[0]=2
print(ls)
d=dict(name="Lucy",age=8,hobby=("bike","game"))
print(d)
print(d["hobby"])
d["age"]=9
print(d)
d["gender"]="F"
print(d)
del d['hobby']
print(d)