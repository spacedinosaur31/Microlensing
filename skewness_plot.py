import pyarrow.parquet as pq
from pandas import DataFrame
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
df = pq.read_table("ztf_000245_zg_c01_q1_dr11.parquet").to_pandas()
lc_table = df.loc[2] 

print(lc_table) #len(mag) = 37
mag1 = lc_table["mag"]
mag = []
for i in mag1:
    mag.append(i)

x = mag
x.sort()
x_mean = np.mean(x)
x_std = np.std(x)
pdf = norm.pdf(x, x_mean, x_std)
plt.plot(x, pdf)
plt.show()