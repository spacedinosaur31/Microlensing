import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
import os #functions for interacting with operating system
from scipy.stats import skew
from vonNeumannstats import neumann as nm

# allskews = []
# allstd = []
# allnepochs = []
# allmeans = []
# lc = []
allnms = []
dir = "C:\Kanti\Microlensing\Python\data\ZTF\lc_dr11"
for root, dirs, files in os.walk(dir):
    a_filtered_def = [] #definitive Liste: falls jede Bedingung erfüllt wurde, LC in Liste einfügen
    for i in files:
#LC-Paket-Tabelle 
        df = pq.read_table(os.path.join(root, i)).to_pandas()
        pd_allLC = df.loc[:] 
        a_lc_list = pd_allLC.iterrows()  #pd = pandas dataframe 

        #alle Lichtkurven aus df, pd = Pandas Dataframe
        #df.loc[:8712] = pandas Dataframe -> als Spalten organisiert
        for k in a_lc_list: # ".iterrows() gibt alle als Zeilen wie
            # print('id',i[0]) 
        
            #type(lc1) == tuple(number, table)import pyarrow.parquet as pq
            lc = k[1]
            if nm(lc[8]):
                allnms.append(nm(lc[8]))

            # allskews.append(skew(lc[8]))

            # allstd.append(np.std(lc[8]))

            # allnepochs.append(lc[6])

            # allmeans.append(np.mean(lc[8]))

            
print(np.mean(allnms))
# OUTPUT: -0.22994225279524635 0.15856555 26.12889056645777 20.421268
