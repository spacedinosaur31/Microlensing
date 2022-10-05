# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:38:37 2022

@author: lamia
"""

import pyarrow.parquet as pq

df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()

def catfl(i):
    i = input(catfl())
    x = df.loc(input(catfl()))
    catf = x["catflags"]
    for i in x:
        for i in catf:
            if i != 0:
                print(catf) 
            else: print("ok")
       
        
catfl(1)