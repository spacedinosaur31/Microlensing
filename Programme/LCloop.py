# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:55:42 2022

@author: lamia
"""
import pyarrow.parquet as pq
import ztfquery
from pandas import DataFrame
import numpy as np

#LC-Paket-Tabelle 
df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
print(len(df))
#df.loc -> erste Spalte 
#for i in df.loc[range(len(df))]:
print(df.count())
allLC = df.loc[:] #alle Lichtkurven aus df
print(allLC.count())
counter=0
#df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
for lc in allLC.iterrows(): # ".iterrows() gibt alle als Zeilen wieder
    counter=counter+1
    if counter > 100: #erste 100 Lichtkurven 
        break
    print("***********  ",counter," ***************")
    print(lc) #type(lc) == tuple(number, table)

allLC.to_excel("100LC.xlsx") # für Funktionen Pandas Dataframe methods googeln


    
 


# inexistente Nummern wegfiltern -> je nach Stelle Nummer geben