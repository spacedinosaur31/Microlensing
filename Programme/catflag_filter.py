# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:53:43 2022

@author: lamia
"""

import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np

#LC-Paket-Tabelle 
df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
#df.loc -> erste Spalte 
#print(df.count())
allLC = df.loc[:] #alle Lichtkurven aus df
print(len(allLC))
counter=0 #index
num = 0 #Anzahl
#df.loc[:] = pandas Dataframe -> als Spalten organisiert
for lc in allLC.iterrows(): # ".iterrows() gibt alle als Zeilen wieder
    lc1 = lc[1]
    for n in lc1: #für lc1[x] -> entweder Magnitude, catflags,...
        counter = counter + 1
        catfl = lc1["catflags"]
        for i in catfl:
          if i != 0 :
              num = num + 1
              print(counter, num, catfl)
    #print(lc) #type(lc) == tuple(number, table)