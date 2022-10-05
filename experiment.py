import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
from collections import Counter
import os as urs #functions for interacting with operating system
from scipy.stats import skew

lclist = [] #definitive Liste: falls jede Bedingung erfüllt wurde, LC in Liste einfügen
truthlst = []
truetruth_lst = []
filterlst = []
skewlist = [] 
stdlist = []
kindnessfac = 0.1
oidlist = []
dir = "C:\Kanti\Microlensing\Python\Parquet-Files"
for root, dirs, files in urs.walk(dir):
    for i in files:
#LC-Paket-Tabelle 
        df = pq.read_table(urs.path.join(root, i)).to_pandas()
        pd_allLC = df.loc[:] 
        a_lc_list = pd_allLC.iterrows()  #pd = pandas dataframe 

        filternumber = 3 #Anzahl Filter
        #df.loc -> erste Spalte 

        #alle Lichtkurven aus df, pd = Pandas Dataframe
        #df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
        for k in a_lc_list: # ".iterrows() gibt alle als Zeilen wie
            # print('id',i[0]) 
        
            ctr = 0
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
                #a_filtered_def.append(lc[0])
                lclist.append(lc[8])
                truthlst.append(0)
                truetruth_lst.append(0)
            
#print(a_filtered_def)
#(len(a_filtered_def)) #Anzahl LC wurde auf 1/8 reduziert
filternumber = 2
for lc in lclist:

    mean = np.mean(lc) #Mittelwert
    std = np.std(lc)

    # #function must be defined in order to fit, m ist fitting parameter
    # def a(time, m): #time = t linspace
    #     if time == numbers:
    #         q = time + 50
    #         return a_nonone[q]*m

    #skewness & kurtosis
    skewlist.append(skew(lc))
    stdlist.append(np.std(lc))
for i in skewlist:
    if i > np.mean(skewlist) - kindnessfac*np.std(skewlist): #Minus weil sonst zu streng, lieber zu viel erkannt als eine nicht erkannt -> garantiert keine ML gehen verloren (wahrscheinlich doch unnötig nach Überprüfung, doch mal beibehalten)
        filterlst.append(skewlist.index(i))
for i in stdlist:
    if std > np.mean(stdlist) - kindnessfac*np.std(stdlist): #np.std weil dann individuell angepasster
        filterlst.append(stdlist.index(i))
    #Standardabweichung

for i in range(len(lclist)): 
    if filterlst.count(i) == filternumber: #hat jeweiliger Index i alle Tests bestanden?
        truthlst[i] = 1 # Lichtkurve an gewisser Stelle alle Filter bestanden -> gleiche Stelle in truthlst mit 1 markieren


lost = []
trap = []
found = []
for i in range(len(lclist)):
    if truthlst[i] != truetruth_lst[i]:
        if truthlst[i] - truetruth_lst[i] < 0: #wenn ML verloren ging
            lost.append(1)
        else:
            trap.append(1) #angebliches ML
    elif truthlst[i] + truetruth_lst[i] == 2.0:
        found.append(1)
        oidlist.append(lc[0])

#print("TEST (-> Fehlversuch falls 0): ", np.count_nonzero(truthlst == 1))#?????
if np.count_nonzero(truthlst == 1) != 0: #wenn kein sog "Fehlversuch"
    print("verlorene ML: ", len(lost))
    print("scheinbare ML: ", len(trap))
    print("gefundene ML: ", len(found))
    print(truetruth_lst)
    print(truthlst)
    print(oidlist)