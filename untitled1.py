# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:11:36 2021

@author: lamia
"""

from alerce.core import Alerce
alerce = Alerce()


dataframe = alerce.query_objects(
    classifier="lc_classifier",
    class_name="LPV",
    format="pandas"
)
print(dataframe.get)