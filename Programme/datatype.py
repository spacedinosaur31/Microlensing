import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
from collections import Counter

#LC-Paket-Tabelle 
df = pq.read_table('C:\Kanti\Microlensing\Python\Parquet-Files\ztf_000870_zg_c02_q2_dr7.parquet').to_pandas()
list_allLC = df.values.tolist() #converts pandas-Dataframe to list
#pd_allLC = df.loc[:] 
print(type(list_allLC))#list
print(len(list_allLC))
for i in range(12):
    print("type(list_allLC[0][", i, "]): ", type(list_allLC[0][i]))
print("type(lightcurve-list) ", type(list_allLC[0])) #list 
  