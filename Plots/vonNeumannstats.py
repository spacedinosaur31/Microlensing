from cmath import nan
import numpy as np

def neumann(array):
    nlst = np.zeros(len(array))
    std = 0.15856555
    for i in range(1, len(array)):
        if len(array) == 1: 
            nlst[i] = ((array[i] - array[i-1])**2)/((len(array)+0.9999999)*(std**2))
        else: 
            nlst[i] = ((array[i] - array[i-1])**2)/((len(array)+1)*(std**2))
    n = np.sum(nlst)
    return n

