def skew(x):
    import numpy as np
    from scipy.stats import norm, skew, kurtosis
    from matplotlib import pyplot as plt
    
    x = input() #synthLC wird eingefügt

    x.sort() #sonst chaotisches herumspringen
    x_mean = np.mean(x) #Mittelwert
    x_std = np.std(x) #Standardabweichung
    pdf = norm.pdf(x, x_mean, x_std) #probability distribution function
    return ("Kurtosis: ", kurtosis(x)), ("Skewness: ", skew(x))
