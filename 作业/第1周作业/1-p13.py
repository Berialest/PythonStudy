# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:29:35 2020

@author: user
"""

s=0
for i in [1,3,5,7,9]:
    s+=i
for i in range(0,10,2):
    print(i)
sum=0
x=input("Input a number (<Enter>'' to quit): ")
while x !="":
    sum=sum+eval(x)
    x=input("Input a number (<Enter> '' to quit): ")