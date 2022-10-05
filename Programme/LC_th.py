# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:22:25 2022

@author: lamia
"""
import matplotlib.pyplot as plt
import numpy as np
import pyarrow.parquet as pq

#A = Magnitude
df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001896_zr_c10_q3_dr7.parquet').to_pandas()
lc1 = df.loc[2] 
mag = lc1['mag']
date = lc1['hmjd']
D_ol = 1 #in AU Abstand Erde-Linse    #freier Parameter
D_ls = 1 #in AU Abstand Linse_Quelle   #freier Parameter
D_os = 1 #in AU Abstand Erde-Quelle    #freier Parameter
b = 1 #in AU Verschiebung der Linse aus Erde-Quelle-Linie
M = 10000000000 #Masse in kg
G = 0.0000000000667408 #konst.
c = 0.02#AU/s
t = [range(1,50000)] #bei linspace: (start, end, Anz. Striche zwischen start und end) -> x-Achse
#freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
count = 0 
# r_e = np.sqrt(((4*G*M)/c*c)*((D_ol*D_ls)/D_os)) #Einstein-Radius
#for x in range(1, 10): #in astronomical units -> closest star to furthest star in milky way 
 #   D_ol = x*t
#for i in range(1, 10):
 #   D_ls = i*t
#    b = i
#    M = i


def A(i):  #Magnitude A abhängig von u, u abhängig von r_e, r_e abhängig von freien Parametern,
# welche von t abhängig sind
    global D_ol, D_ls, D_os#mit D_xx ist die globale Variable (oben definiert) gemeint
    
    print(t)
    for x in t:
      D_ol = D_ol - t
      D_ls = x*D_ls 
      D_os = (x**2 + 150)*D_os 
      r_e = ((4*G*M)/(c*c))*((D_ol*D_ls)/D_os)**(1/2)
      
    u = b/r_e

    for i in u:
        
        if i <= 0.5:   #solange u kleiner als 0.5 ist, wird die Magnitude durch 1/u definiert
         A = 1/i

    # u > 2
    # while True: 
    #    A = 1 + 2*u**(-4)
       
        else:
          A = (i**2 + 2) / (i*(i**2 + 4))**(1/2)
    return A 

plt.figure()
plt.plot(t, A(t),"-", color = "red")
plt.show()