# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:35:10 2022

@author: System Administrator
"""
count = 0
with open("D:\\LAGACY_TRAIN\\bagaliy_word_list.txt",mode = 'r', encoding="utf-8") as f:
    for i,line in enumerate(f):
        count = count + 1
print(count)