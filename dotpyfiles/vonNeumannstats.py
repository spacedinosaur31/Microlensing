import numpy as np

def neumann(array):
    nlst = np.zeros(len(array))
    std = np.std(array)
    for i in range(1, len(array)):
        nlst[i] = ((array[i] - array[i-1])**2)/((len(array)-1)*(std**2))
    n = np.sum(nlst)
    return n

