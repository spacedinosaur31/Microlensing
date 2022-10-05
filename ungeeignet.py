# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:59:43 2022

@author: lamia
"""
import pyarrow.parquet as pq

#inexistente Nummern (1. Spalte)
df = pq.read_table('C:/Kanti/Microlensing/ztf_000468_zi_c16_q4_dr7.parquet').to_pandas()
print(df)
filterid =
lc1 = df.loc[]
