# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:53:10 2021

@author: lamia
"""
import dask.dataframe as dd
ddf = dd.read_parquet('ztf_000202_zg_c10_q1_dr7.parquet', engine='pyarrow')
print(ddf)
