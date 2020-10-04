# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:26:06 2020

@author: user
"""
i = 0
a = input("输入学生姓名，用英文逗号隔开，输入回车结束：")
a = a.split(",")
i = 1
while True:
    check = input("需要检索的姓名,输入0结束检索：")
    if check == "0":
        break
    if check in a :
        print(check+"已保存在列表中")
    else:
        print(check+"未保存在列表中")