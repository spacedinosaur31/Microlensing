import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np

#LC-Paket-Tabelle 
df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
lim = 20
#df.loc -> erste Spalte 
#print(df.count())
allLC1 = df.loc[:] #alle Lichtkurven aus df
allLC = allLC1.iterrows()
counter=0
#df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
for lc1 in allLC: # ".iterrows() gibt alle als Zeilen wieder
    counter=counter+1
    lc = list(lc1) #sollte tuple in Liste konvertieren
    lc[0] = counter
    if np.absolute(list(allLC[allLC.index(lc1)-1][8]) - lc[1][8]) > 20:
        print(lc1["oid"])