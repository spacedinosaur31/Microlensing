import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
import os #functions for interacting with operating system
from matplotlib import pyplot as plt
from scipy.stats import skew

# VALUES
t0 = 0 # Zeitpunkt max. Helligkeit
mean_skew = 22994225279524635 #Mittelwert von 2 fields
max_skew = -0.9  
mean_std = 0.15856555  # Mittelwert von 2 fields
mean_mag = 20.421268  # Mittelwert von 2 fields
mean_luminosity = 10**(mean_mag/(-2.5)) # convert magnitude-mean to luminosity-value for multiplication by amplification factor
max_neumann = 1.5 # circa

# LISTS
a_filtered_vorfilter = [] 
a_filtered_grobfilter = []

dir = "C:\Kanti\Microlensing\Python\data"
for root, dirs, files in os.walk(dir):
    for i in files:
#LC-Paket-Tabelle 
        df = pq.read_table(os.path.join(root, i)).to_pandas()
        allLC_list = df.values.tolist()  #convert pandas dataframe to list
        for lc in allLC_list: # ".iterrows() gibt alle als Zeilen wie
            #AB HIER FILTER EINFÜGEN

            catfl = lc[11] #type(catfl) = numpy.ndarray
            nepochs = lc[6] #Anzahl Messpunkte
            filter = lc[1] #r, g or i -> only r
            if sum(catfl) == 0 and nepochs > 30 and filter == 2: 
                a_filtered_vorfilter.append(lc)


# SYNTHETIC LC GENERATOR + FILTERING -> Produktion künstlicher LC -> random ML-Events oder nicht 
for lc in a_filtered_vorfilter:  
    mag = lc[8]
    t = lc[7]
    neumann_lst = np.zeros(len(mag))
    std = np.std(mag)
    for i in range(1, len(mag)):
        neumann_lst[i] = ((mag[i] - mag[i-1])**2)/((len(mag)-1)*(std**2))
    n = np.sum(neumann_lst)
    count = 0
    if (skew(mag) < max_skew) and (n < max_neumann):
        a_filtered_grobfilter.append(lc)
        
print("LC-Menge vorher: ", len(allLC_list))
print("LC-Menge nachher: ", len(a_filtered_grobfilter))
