import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
from collections import Counter

#LC-Paket-Tabelle 
df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
pd_allLC = df.loc[:] #df.iloc?
a_lc_list = pd_allLC.iterrows()  #pd = pandas dataframe 

filternumber = 2 #Anzahl Filter
#df.loc -> erste Spalte 

#alle Lichtkurven aus df, pd = Pandas Dataframe
#df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
a_filtered = [] #falls LC eine Bedingung erfüllt, wird Index in Liste eingefügt
a_filtered_def = [] #definitive Liste: falls jede Bedingung erfüllt wurde, LC in Liste einfügen
for i in a_lc_list: # ".iterrows() gibt alle als Zeilen wie 
    #type(lc1) == tuple(number, table)import pyarrow.parquet as pq
    lc = i[1] #ab hier verschiedene Filter einfügen
    #für lc1[x] -> entweder Magnitude, catflags,...


    catfl = lc[11] #type(catfl) = numpy.ndarray
    #print(type(lc)) 
    for j in catfl:
        if j != 0: #falls keine catflags, füge Object-ID in array ein
            break
        else: 
            a_filtered.append(lc[0])


    mag = lc[8] ##type() = numpy.ndarray
    #Anzahl Datenpunkte

    for x in mag: # ".iterrows() gibt alle als Zeilen wieder
        if lc[6] < 20: #falls zu wenige Datenpunkte: raus
            break
        else:
            counter=1
            counter = counter + 1 #jedem Magnituden-Datenpunkt Nummer geben
            counter2 = 0 #zählt eins dazu, wenn Differenz zu gross ist
            #Rauschen
            if np.absolute(mag[counter] - mag[counter - 1]) > 10: #Grosse aufeinanderfolgende Magnitudendifferenzen zählen (counter2)
                counter2 = counter2 + 1
                if counter2 < 10: #falls zu viele Differenzen zwischen aufeinanderfolgenden Datenpunkten (chaotisches Rauschen) -> LC raus
                    a_filtered.append(lc[0])
        
    if Counter(a_filtered)[lc[0]] == filternumber: #Counter(a_filtered)[lc[0]] -> zählt wie oft Zahl bei lc[0] in array vorkommt (ob alle Bedingungen erfüllt sind)
        a_filtered_def.append(lc[0])

#print(a_filtered_def)
print(len(a_lc_list))
print(len(a_filtered_def)) #Anzahl LC wurde auf 1/8 reduziert
        
        #konstante LC??
            

         
