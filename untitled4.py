# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:44:25 2022

@author: lamia
"""
# R = realer Teil
# i = imaginärer Teil 
for R in range(-20,20):
    for Im in range(-10,20, 1):
        quadr = R^2 - Im^2 + 2*R*Im
        while quadr > 1:
            print(1)
            break
        else: 
            print(quadr, R, Im)
            break
    