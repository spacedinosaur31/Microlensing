# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:42:22 2021

@author: lamia
"""
from ztfquery import lightcurve
#data = lightcurve.LCQuery.download_data(circle=[298.0025,29.87147,0.0014], bandname="g")
lcq = lightcurve.LCQuery.from_id('ZTF17aaaaaam')
#lcq = lightcurve.LCQuery(data)
lcq.show()

#df = pq.read_table('0/field0202').to_pandas()