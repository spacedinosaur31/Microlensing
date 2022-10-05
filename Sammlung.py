# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:37:51 2022

@author: lamia
"""
list = [0,2,4,6,22]

# Differenz zweier Objekte einer Liste
for i in range(len(list)):
    diff = list[i]-list[i-1]
    if i != 0:
        print(diff)
