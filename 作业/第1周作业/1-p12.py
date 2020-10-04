# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:04:21 2020

@author: user
"""

s=input("姓名和年龄：")
name,age=s.split(",")#用“，”切分字符串
print(name,age)#屏幕输出
print("name:{},age:{}".format(name,age))#格式化输出