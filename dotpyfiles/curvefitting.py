from scipy.optimize import curve_fit as fit
import numpy as np
from synthfilter5 import filteredlc
from matplotlib import pyplot as plt

filtered_lc_lst = filteredlc()
filteredLCamount = len(filtered_lc_lst)
fittedlst = []
maxcov = 1 #maximale Kovarianz -> ?
def theo(t, umin, tE):
    t_0 = 0
    u = np.sqrt(umin**2 + ((t-t_0)/tE)**2)
    A = (u**2 + 2) / (u*np.sqrt(u**2 + 4)) 
    M = -2.5*np.log10(A) 
    return M
for i in range(filteredLCamount):
    id = filtered_lc_lst[i][0] 
    mag = filtered_lc_lst[i][1] 
    t = filtered_lc_lst[i][2] 
    try: #try-except-thing causes loop to continue when error occurs
        fitted_params, param_covariance = fit(theo, t, mag, p0 = [0.5, 150]) #input th=Funktion, die gefittet werden soll, t=unabhängige Variable, a=Messwerte, p0 = initial guesses
        umin_fit = fitted_params[0]
        tE_fit = fitted_params[1]
        if (0.0 < umin_fit <= 1.0):
            fittedlst.append([id, fitted_params, param_covariance])
            print("*** Parameters:", fitted_params,"*** Covariance:", param_covariance, "***")
    except:
        pass

# #print(filteredlclst)