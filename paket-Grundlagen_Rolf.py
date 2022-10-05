import pyarrow.parquet as pq
import ztfquery
import matplotlib.pyplot as plt
import numpy as np

df = pq.read_table('ztf_001575_zr_c16_q4_dr7.parquet').to_pandas()
#print(df)
len=df.shape
print(len[0])
lc1 = df.loc[4] 
# objectid = lc1['objectid']  
# filterid = lc1['filterid']   
# fieldid = lc1['fieldid']   
# rcid = lc1['rcid']   
# objra = lc1['objra']   
# objdec = lc1['objdec']   
# nepochs = lc1['nepochs']   
# magerr = lc1['magerr']
# clrcoeff = lc1['clrcoeff']
# catflags = lc1['catflags']
hmjd = lc1['hmjd'] 
mag = lc1['mag']

goodloci=np.zeros(len[0])
j=0
for i in range(0,len[0]-1):
    if (df.iloc[i]['nepochs']>=20):
        goodloci[j]=i
        j+=1

goodloci=goodloci[0:j]

print(goodloci)
print(j)

# print(objectid)
# print(filterid)
# print(fieldid)
# print(rcid)
# print(objra)
# print(objdec)
# print(nepochs)
# print(hmjd)
# print(mag)
# print(magerr)
# print(clrcoeff)
# print(catflags)

out=open('objfilt.txt','w')
for step in range(0,len[0]):
    out.write('%i %g\n' % (df.iloc[step]['objectid'],df.iloc[step]['filterid']))
out.close

plt.plot(hmjd, mag, '.', color = 'red')

