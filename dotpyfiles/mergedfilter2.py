from asyncio import ALL_COMPLETED
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

        a_a_all_LC_original = o_pandas_data_frame.values #makes np.array()
        
        # if(a_a_value__original_merged == None):
        #     a_a_value__original_merged = numpy.copy(a_a_value__original)
        # else: 
        #     a_a_value__original_merged = numpy.concatenate((a_a_value__original_merged, a_a_value__original))

#make filtered list right away
        a_a_objectid_filtered.append( 
            a_LC[o_indices.objectid]# a_value # 'return value'
            for
            a_LC # variable name in loop
            in a_a_all_LC_original  # array name of iterated array

            if (
                a_LC[o_indices.catflags].sum() == 0 
                and a_LC[o_indices.nepochs] > 30
                and a_LC[o_indices.filterid] == 2 
            )  # if this is true, 'return value' is returned
        )

a_a_skew_nm_lc_filtered = numpy.array()

for s_path_root, a_s_folder, a_s_file in os.walk(dir):
    for s_file in a_s_file:
        o_table = pyarrow.parquet.read_table(
                os.path.join(s_path_root, s_file)
            )

        o_pandas_data_frame = o_table.to_pandas()

        a_a_all_LC_original = o_pandas_data_frame.values #makes np.array()
        
        a_a_skew_nm_lc_filtered.append(
            a_LC for a_LC in a_a_all_LC_original
            if
            numpy.skew(a_LC[o_indices.mag]) <= (10**((neumann(a_LC) - c)/a) - b)  
        )

with open(f"./filtered/{s_file}_filtered.npy", 'wb') as o_file:
        numpy.save(o_file, a_a_value__filtered)        
        # o_pandas_data_frame_filtered = pandas.DataFrame(
        #     a_a_value__filtered, 
        #     columns = o_pandas_data_frame.columns
        # )
        # o_pandas_data_frame_filtered = pandas.DataFrame(
        #     data = a_a_value__filtered,
        #     index=o_pandas_data_frame.index,
        #     columns=o_pandas_data_frame.columns
        # )
        # o_pandas_data_frame_filtered = pd.DataFrame().reindex_like(df_original)
        # pd.DataFrame(
        #     data=o_pandas_data_frame_filtered[1:,1:],    # values
        #     index=data[1:,0],    # 1st column as index
        #     columns=data[0,1:]
        # )  # 1st row as the column names

        # pyarrow.parquet.write_table(
        #     "testparquestout", 
        #     o_pandas_data_frame_filtered
        # )

        #     def filter_fromiter(arr, cond):
        # return numpy.fromiter((x for x in arr if cond(x)), dtype=arr.dtype)
        # a_a_value__filtered = numpy.array(a_a_value__filtered)

        # o_dtype = numpy.dtype(o_pandas_data_frame.columns)
        # print(a_type)
        # print(a_type)
        # print(a_type)
        # exit(1)      
        # a_a_value_filtered = numpy.array( # Problem: make sth similar to .parquet with columns + column names
        #     a_a_all_LC_original[o_indices.objectid] #so sieht man beim Index angeben gleich, was es ist
            # )
            # [
            #     (s,s)
            #     for 
            #     s 
            #     in 
            #     o_pandas_data_frame.columns
            # ]
            # o_pandas_data_frame.dtype
            
        # a_a_value__filtered.dtype = o_dtype


# print(a_a_value__original[0][o_indices.objectid])

# print(a_a_value__original_merged)

# a_a_value__filtered = [ 
#     # a_value # 'return value'
#     a_value# 'return value'
#     for
#     a_value # variable name in loop
#     in a_a_value__original_merged  # array name of iterated array

#     if (
#         a_value[o_indices.catflags].sum() == 0 
#         and a_value[o_indices.nepochs] > 3
#     )  # if this is true, 'return value' is returned
# ]

# a_a_value__original_filtered = a_a_value__original_filtered + a_a_value__filtered

# print("len(a_a_value__original)")
# print(len(a_a_value__original))
# print("len(a_a_value__filtered)")
# print(len(a_a_value__filtered))

# print(a_a_value__filtered_merged)

# print(a_a_value__filtered)

# 1.25 seconds per 2500 rows 

        # a_a_value[]

        # o_combinaion = o_house + o_dog 
        # a_a_value[0] # 
        # print(a_a_value)


        # print(o_pandas_data_frame.values[0])

        # allLC_list = df.values.tolist()  #convert pandas dataframe to list
        # print(allLC_list[0][0])
#         for lc in allLC_list: 
#             #AB HIER FILTER EINFÜGEN
#             print(lc)
        

#             catfl = lc[11] #type(catfl) = numpy.ndarray
#             nepochs = lc[6] #Anzahl Messpunkte, type(nepochs) = int
#             filterid = lc[1] #g (1), r (2) or i (3) -> only r, type(filter) = int
#             if sum(catfl) == 0 and nepochs > 30 and filterid == 2: 
#                 a_filtered_vorfilter.append(lc)

# print(a_filtered_vorfilter)
      
# #Grobfilter: zu hohe Skewness & zu hoher Neumann-Statistik-Wert raus
# for lc in a_filtered_vorfilter:  
#     mag = lc[8]
#     t = lc[7]
#     neumann_lst = np.zeros(len(mag))
#     std = np.std(mag)
#     for i in range(1, len(mag)):
#         neumann_lst[i] = ((mag[i] - mag[i-1])**2)/((len(mag)-1)*(std**2))
#     n = np.sum(neumann_lst)
#     if (skew(mag) < max_skew) and (n < max_neumann):
#         a_filtered_grobfilter.append(lc)
#         # plt.title(lc[0])
#         # plt.plot(t, mag, ".", color = "red")
        
# print("LC-Menge nachher: ", len(a_filtered_grobfilter))

# #save list in .txt for later use
# with open('a_filtered_grobfilter.txt', 'w') as f:
#     f.write(str(a_filtered_grobfilter))
