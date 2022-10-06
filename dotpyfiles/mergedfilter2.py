import pyarrow.parquet
import pandas 
import numpy 
import os #functions for interacting with operating system
from matplotlib import pyplot as plt
from scipy.stats import skew
import json

# VALUES
max_skew = -0.9  
max_neumann = 1.5 # circa, in work

# LISTS
a_filtered_vorfilter = [] 
a_filtered_grobfilter = []

# FUNCTIONS
def neumann(array):
    neumann_lst = numpy.zeros(len(array))
    std = numpy.std(array)
    for i in range(1, len(array)):
        neumann_lst[i] = ((array[i] - array[i-1])**2)/((len(array)-1)*(std**2))
    neumann_value = numpy.sum(neumann_lst)
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

o_indices = O_indices()
a_a_objectid_filtered = []




for s_path_root, a_s_folder, a_s_file in os.walk(dir):
    for s_file in a_s_file:
        o_table = pyarrow.parquet.read_table(
                os.path.join(s_path_root, s_file)
            )

        o_pandas_data_frame = o_table.to_pandas()

        a_a_all_LC = o_pandas_data_frame.values #makes np.array()
        
        # if(a_a_value__original_merged == None):
        #     a_a_value__original_merged = numpy.copy(a_a_value__original)
        # else: 
        #     a_a_value__original_merged = numpy.concatenate((a_a_value__original_merged, a_a_value__original))

#make filtered list right away
        a_a_all_LC = numpy.array([ 
            a_LC# a_value # 'return value'
            for
            a_LC # variable name in loop
            in a_a_all_LC  # array name of iterated array
            if (
                a_LC[o_indices.catflags].sum() == 0 
                and a_LC[o_indices.nepochs] > 30
                and a_LC[o_indices.filterid] == 2
            )  # if this is true, 'return value' is returned
        ])

        a_a_all_LC = numpy.array([
            a_LC for a_LC in a_a_all_LC
            if
            (numpy.skew(a_LC[o_indices.mag]) <= (10**((neumann(a_LC) - c)/a) - b)) #params in work
        ])

        os.rename(s_file, s_file + "_filtered")
        
# #save list in .txt for later use
# with open('a_filtered_grobfilter.txt', 'w') as f:
#     f.write(str(a_filtered_grobfilter))
