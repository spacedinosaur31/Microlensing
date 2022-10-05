import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
import os #functions for interacting with operating system
from matplotlib import pyplot as plt
from scipy.stats import skew

# VALUES
max_skew = -0.9  
max_neumann = 1.5 # circa, in work

# LISTS
a_filtered_vorfilter = [] 
a_filtered_grobfilter = []

dir = "C:\Kanti\Microlensing\Python\Parquet-Files" #path to root directory 
for root, dirs, files in os.walk(dir):
    for i in files:
#LC-Paket-Tabelle 
        df = pq.read_table(os.path.join(root, i)).to_pandas()
        allLC_list = df.values.tolist()  #convert pandas dataframe to list
        for lc in allLC_list: 
            #AB HIER FILTER EINFÜGEN

            catfl = lc[11] #type(catfl) = numpy.ndarray
            nepochs = lc[6] #Anzahl Messpunkte, type(nepochs) = int
            filterid = lc[1] #g (1), r (2) or i (3) -> only r, type(filter) = int
            if sum(catfl) == 0 and nepochs > 30 and filterid == 2: 
                a_filtered_vorfilter.append(lc)
      
#Grobfilter: zu hohe Skewness & zu hoher Neumann-Statistik-Wert raus
for lc in a_filtered_vorfilter:  
    mag = lc[8]
    t = lc[7]
    neumann_lst = np.zeros(len(mag))
    std = np.std(mag)
    for i in range(1, len(mag)):
        neumann_lst[i] = ((mag[i] - mag[i-1])**2)/((len(mag)-1)*(std**2))
    n = np.sum(neumann_lst)
    if (skew(mag) < max_skew) and (n < max_neumann):
        a_filtered_grobfilter.append(lc)
        # plt.title(lc[0])
        # plt.plot(t, mag, ".", color = "red")
        
print("LC-Menge nachher: ", len(a_filtered_grobfilter))

#save list in .txt for later use
with open('a_filtered_grobfilter.txt', 'w') as f:
    f.write(str(a_filtered_grobfilter))
