import numpy as np
from matplotlib import pyplot as plt
import manyLC_synth as mlc
from scipy.stats import norm, skew, kurtosis
from scipy.optimize import curve_fit as fit
import random
import numbers
countlosses = []
for i in range(500):

    LCamount = 100
    truthlst = np.zeros(LCamount)
    lclist = []
    skewlist = []
    stdlist = []
    kurtlist = []
    filterlst = []
    filternumber = 2
    min_std = 0.4
    truetruth_lst = np.zeros(LCamount) #np.zeros(x) macht Liste mit x Nullen
    frequency = 3 #1 Messung in x Tagen -> 100/3 -> insgesamt ca. 30 Datenpunkte (wie in Paper)
    probability = 2
    kindnessfac = 0.2

    #LC-Parameter:
    t0=0 #Zeitpunkt max. Helligkeit
    umin=0.25
    tE=25 #Zeitdauer, um Einstein-Radius zurückzulegen
    standard_deviation = 0.4

    for i in range(0, LCamount): #length random Lichtkurven werden generiert
        #Produktion von künstlichen Lichtkurven
        l = random.randint(0, 5) #Helligkeit Stern
        p = random.randint(0, probability) #Wahrscheinlichkeit von 1/40

        if p == 1:
            truetruth_lst[i] = 1 #Nullen-Array an x-ter Stelle mit 1 ersetzt -> ML-Event
            # t0=0 #Zeitpunkt max. Helligkeit
            # umin=0.25
            # tE=25 #Zeitdauer, um Einstein-Radius zurückzulegen
            # standard_deviation = 0.2

            t = np.linspace(-50, 50, 100) #(start, end, Anz. Striche zwischen start und end) -> x-Achse
            #freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
            a = []
        
            for d in t:  #Helligkeit A abhängig von u, u abhängig t
                y = random.randint(0, frequency) #Messung ca. einmal in 30 Tagen
                if y == 1: 
                    u = np.sqrt(umin**2 + ((d-t0)/tE)**2)
                    A = (u**2 + 2) / (u*np.sqrt(u**2 + 4)) + random.gauss(0, standard_deviation) #bei beiden Gauss-Rauschen machen
                    a.append(A)
                else: 
                    a.append(None)
            lclist.append(a)

        if p != 1: 
            mean = 4 #randomize -> bei ZTF nachschauen -> uniform()
            #standard_deviation = 0.5
            
            t = np.linspace(-50, 50, 100) #(start, end, Anz. Striche zwischen start und end) -> x-Achse
            
            a = []
            
            for d in t:
                y = random.randint(0, frequency)
                if y == 1:
                    A = mean + random.gauss(0, standard_deviation)
                    a.append(A)
                else:
                    a.append(None)
            lclist.append(a)

    for lc in lclist:

        #***********HIER FILTER EINFÜGEN************

            #Theoriewerte generieren
        t = np.linspace(-50, 50, 100) #(start, end, Anz. Striche zwischen start und end) -> x-Achse
        #freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
        a = [] 
        frequency = 10
        
        for i in lc:
            if i is None:
                a.append(None)
            else:
                u = np.sqrt(umin**2 + ((t-t0)/tE)**2)
                A = (u**2 + 2) / (u*np.sqrt(u**2 + 4)) #bei beiden Gauss-Rauschen machen
                a.append(A)

        #make comparable lists -> None-values cause errors
        lc_nonone = []
        for i in lc:
            if i is not None:
                lc_nonone.append(i)
        a_nonone = []
        for i in a:
            if i is not None:
                a_nonone.append(i)

        mean = np.mean(lc_nonone) #Mittelwert
        std = np.std(lc_nonone)

        # #function must be defined in order to fit, m ist fitting parameter
        # def a(time, m): #time = t linspace
        #     if time == numbers:
        #         q = time + 50
        #         return a_nonone[q]*m

        #skewness & kurtosis
        skewlist.append(skew(lc_nonone))
        stdlist.append(np.std(lc_nonone))
    for i in skewlist:
        if i > np.mean(skewlist) - kindnessfac*np.std(skewlist): #Minus weil sonst zu streng, lieber zu viel erkannt als eine nicht erkannt -> garantiert keine ML gehen verloren (wahrscheinlich doch unnötig nach Überprüfung, doch mal beibehalten)
            filterlst.append(skewlist.index(i))
    for i in stdlist:
        if std > np.mean(stdlist) - kindnessfac*np.std(stdlist): #std weil dann individuell angepasster
            filterlst.append(stdlist.index(i))
        #Standardabweichung

    if np.count_nonzero(truetruth_lst == 0) != LCamount: #no ML-Event -> false trues
        for i in range(LCamount):
            if filterlst.count(i) == filternumber:
                truthlst[i] = 1 # Lichtkurve an gewisser Stelle alle Filter bestanden -> gleiche Stelle in truthlst mit 1 markieren
    
    lost = []
    found = []
    for i in range(LCamount):
        if truthlst[i] != truetruth_lst[i]:
            if truthlst[i] - truetruth_lst[i] < 0: #wenn ML verloren ging
                lost.append(1)
            else:
                found.append(1)

    #print("TEST (-> Fehlversuch falls 0): ", np.count_nonzero(truthlst == 1))#?????
    if np.count_nonzero(truthlst == 1) != 0: #wenn kein sog "Fehlversuch"
        countlosses.append(len(lost))
        #print("verlorene ML: ", len(lost))
        #print("scheinbare ML: ", len(found))
    #print(truetruth_lst)
    #print(truthlst)
print(sum(countlosses))
print("verlorene ML: ", len(lost))
