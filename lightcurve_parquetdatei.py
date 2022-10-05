# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:34:33 2021

@author: lamia
"""
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import datetime

df = pq.read_table('C:/Kanti/Microlensing/LC-Pakete/ztf_001896_zr_c10_q3_dr7.parquet/').to_pandas()
print(df)
lc1 = df.loc[2] 
df.loc[2].to_excel('C:/Kanti/Microlensing', sheet_name="lc_skew")
# # .loc() = Befehl in Pandas, um alle zugehörigen Daten zu gewissem Objekt zu holen 
mag = lc1['mag']
date = lc1['hmjd']

# # oids = df['objectid']
# # for oid in oids:
# #     if oid == 202110100018804:
# #         print(oid)
# print(df.loc[2])   


print(lc1['hmjd'])
# t = np.linspace(date,)
plt.plot(date, mag, '.', color = 'red')
# print(date)
#print(datetime.datetime.strptime(str(int(date[0])), '%y%j').strftime('%d.%m.%Y')) 
# Konvertierung HMJD -> GD; Dezimalstellen wurden nicht erkannt, deshalb int()








