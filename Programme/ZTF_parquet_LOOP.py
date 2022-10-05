# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:55:42 2022

@author: lamia
"""
import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np

#LC-Paket-Tabelle 
df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
#df.loc -> erste Spalte 
print(df.count())
allLC = df.loc[:] #alle Lichtkurven aus df

counter=0
#df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
for lc in allLC.iterrows(): # ".iterrows() gibt alle als Zeilen wieder
    #type(lc) == tuple(number, table)
    
