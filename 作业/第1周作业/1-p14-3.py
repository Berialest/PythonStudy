# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:58:28 2020

@author: user
"""

dic =  {"阿大":160,"阿二":170,"阿三":180,"阿四":190} 
check = input("输入任意同学的姓名:")
for key in dic.keys():
    if dic[key] > dic[check]:
        print("姓名"+key+",身高"+str(dic[key])) 