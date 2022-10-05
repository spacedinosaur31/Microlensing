import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
from collections import Counter
import os #functions for interacting with operating system

a_filtered_def = [] #definitive Liste: falls jede Bedingung erfüllt wurde, LC in Liste einfügen
totlcnum = []
dir = "C:\Kanti\Microlensing\Python\data\ZTF\lc_dr11"
for root, dirs, files in os.walk(dir):
    for i in files:
#LC-Paket-Tabelle 
        df = pq.read_table(os.path.join(root, i)).to_pandas()
        pd_allLC = df.loc[:] 
        a_lc_list = pd_allLC.iterrows()  #pd = pandas dataframe 

        filternumber = 3 #Anzahl Filter
        #df.loc -> erste Spalte 

        #alle Lichtkurven aus df, pd = Pandas Dataframe
        #df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
        for k in a_lc_list: # ".iterrows() gibt alle als Zeilen wie
            # print('id',i[0]) 
            totlcnum.append(1)
            #type(lc1) == tuple(number, table)import pyarrow.parquet as pq
            lc = k[1] 
        
            #AB HIER FILTER EINFÜGEN

            catfl = lc[11] #type(catfl) = numpy.ndarray
        
            cath = []
            ctr = []
            
            for j in catfl:
                cath.append(j)
            if sum(cath) == 0:
                ctr.append(1)
            

            if lc[6] > 30: #falls weniger als 10 Messpunkte -> LC raus
                ctr.append(1)

            if lc[1] == 2: #nur r-filter
                ctr.append(1)
                
            if len(ctr) == filternumber: #zählt wie oft Zahl bei lc[0] in array vorkommt (ob alle Bedingungen erfüllt sind)
                a_filtered_def.append(lc)
                
print(len(totlcnum))            
print(len(a_filtered_def))
#(len(a_filtered_def)) #Anzahl LC wurde auf 1/8 reduziert