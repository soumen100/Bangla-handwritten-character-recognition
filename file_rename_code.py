# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:35:44 2022

@author: System Administrator
"""

import os
folder_to='C:/Users/System Administrator/Documents/soumen_halder/raw_data'
folder_from = 'C:/Users/System Administrator/Documents/soumen_halder/lagacy_train_200'
for i,filename in enumerate(os.listdir(folder_to)):
   # print(filename)
    x = filename.split('_')
    #print(x[0])
    dst = f"ben.{i}.exp{str(i)}.tif"
    src =f"{folder_to}/{filename}" 
    dst1 =f"{folder_from}/{dst}"
    os.rename(src, dst1)