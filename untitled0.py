# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:47:57 2022

@author: lamia
"""

import pyarrow.parquet as pq
import matplotlib.pyplot as plt

df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
#print(df)
lc1 = df.loc[20] 
print(df.loc[3])
mag = lc1['mag']
date = lc1['hmjd']    
#print(lc1)
                                                                                                                                                                    
#print(lc1['mag'])
plt.plot(date, mag, '.', color = 'red')
#print(date)
#for i in range(len(date)):
 #   diff = date[i]-date[i-1]
  #  print(diff)

#Paket runterladen
#...
#Paket in Datenstruktur packen
#...
#Ordner 0 und 1 vergleichen wegen Zeitraum
# ...
#ungeeignete LC wegfitern
#Loop über alle LC, zB auf catflags checken und nicht existente wegfiltern
#Ziel: Array aus Nummern der guten LC
#geeignte Kurven nach Muster absuchen
#Output
#MA fertigschreiben