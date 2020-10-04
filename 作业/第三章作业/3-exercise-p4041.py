# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:07:01 2020

@author: user
"""

from pandas import Series,DataFrame
x=Series([30,25,27,41,25,34],index=['a','b','c','d','e','f'])
print(x)
x1=Series([27],index=['g'])
newx=x.append(x1)
print(newx)
x['d']=40
print(newx)
print(newx[newx.values>27])
print(newx.drop(['b','c','d']))
data=[[1,2,3],[4,5,6],[7,8,9]]
x=DataFrame(data,index=['a','b','c'],columns=['one','two','three'])
print(x)
print(x.loc[:,['three','two']])
print(x.iloc[[0,2]])
print(x.iloc[:,[0,2]])
data1=x[-x.one.isin(x['one']<=2)]
print(data1)
data1['four']=10
print(data1)
data1[data1.values>9]=8
print(data1)
data2=data1.drop(['b','c'],axis=0)
print(data2)
