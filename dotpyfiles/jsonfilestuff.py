import pyarrow.parquet
import pandas 
import numpy as np
import os #functions for interacting with operating system
from scipy.stats import skew
import json
import wget
import time

# LISTS
a_errorfiles = [0 for x in range(163319)]
a_a_objectids_vorfilter = [0 for x in range(163319)]

# FUNCTIONS
def neumann(array):
    neumann_lst = np.zeros(len(array))
    std = np.std(array)
    for i in range(1, len(array)):
        neumann_lst[i] = ((array[i] - array[i-1])**2)/((len(array)-1)*(std**2))
    neumann_value = np.sum(neumann_lst)
    return neumann_value

# dir = "C:\Kanti\Microlensing\Python\Parquet-Files" #path to root directory 
dir = "./data" #path to root directory
dir = "./Parquet-Files" #path to root directory

class O_indices: #object for indices as "objectid", not as "lc[0]", für Übersichtlichkeit
    objectid = 0
    filterid = 1
    fieldid = 2
    rcid = 3
    objra = 4
    objdec = 5
    nepochs = 6
    hmjd = 7
    mag = 8
    magerr = 9
    clrcoeff = 10
    catflags = 11


# Opening JSON file
o_file_0 = open('./a_s_url_https_irsa_ipac_caltech_edu_data_ZTF_lc_lc_dr11_0.json')
o_file_1 = open('./a_s_url__https__irsa_ipac_caltech_edu_data_ZTF_lc_lc_dr11_1.json')
  
# returns JSON object as 
# a dictionary
a_s_url_0 = json.load(o_file_0)
a_s_url_1 = json.load(o_file_1)
a_s_url__merged = a_s_url_0 + a_s_url_1

# a_a_all_LC__example = [
#     #[...],
#     [ 
#        468316400000000, #=> objectid", # 
#        3, #=> filterid", # 
#        468, #=> fieldid",
#        63, #=> rcid",
#        148.4763641357422, #=> objra",
#        7.4226508140563965, #=> objdec",
#        1, #=> nepochs",
#        array([58257.184], dtype=float32), #=> hmjd",
#        array([17.160751], dtype=float32), #=> mag",
#        array([0.02298518], dtype=float32), #=> magerr",
#        array([0.18954925], dtype=float32), #=> clrcoeff",
#        array([0, 1, 2, 4], dtype=uint16), #=> catflags",
#     ], 
#     #[...],
# ]

class O_indices: #object for indices as "objectid", not as "lc[0]"
    objectid = 0
    filterid = 1
    fieldid = 2
    rcid = 3
    objra = 4
    objdec = 5
    nepochs = 6
    hmjd = 7
    mag = 8
    magerr = 9
    clrcoeff = 10
    catflags = 11
o_indices = O_indices()

s_path_current_directory = os.path.dirname(os.path.realpath(__file__))

n_len_a_s_url__merged = len(a_s_url__merged) # 163319
count = [
    1
    for s_url in a_s_url__merged
    if "zr" in s_url
]

print(np.sum(count))