import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, skew, kurtosis
from scipy.optimize import curve_fit as fit
import random

#other values
filternumber = 3
probability = 1
magpointamount = 30
t0=0 #Zeitpunkt max. Helligkeit
surveylength = 500 #wie lange gesamte Messung dauerte = maximale Eventdauer
standard_deviation = 0.2
mean_skew = -0.22994225279524635  #Mittelwert von 2 fields 
mean_std = 0.15856555  #Mittelwert von 2 fields 
mean_mean = 20.421268  #Mittelwert von 2 fields 
mean_nm = 1
C = 0
LCamount = 10

#LISTS
truthlst = [0 for i in range(LCamount)] #Liste gefilterter ML-Events, np.zeros(x) macht Liste mit x Nullen
truetruth_lst = [0 for i in range(LCamount)] #Liste mit tatsächlichen ML-Events
lclist = [0 for i in range(LCamount)] #stellt synthetischen Datensatz dar -> pro LC Liste wie [Index (-> Object-ID), Magnitudenwerte, Zeitpunkte] -> muss Liste sein, da np.array keine arrays speichern kann aber kein Problem, da bei ZTF kein lclist erzeugt werden muss
filterlst = [0 for i in range(LCamount)] #Index (wie object ID) wird in Liste eingefügt -> am Schluss gezählt, ob alle Kriterien erfüllt
skewlist = [0 for i in range(LCamount)] #Skewness-Werte alles LC
stdlist = [0 for i in range(LCamount)] #Standardabw-Werte alles LC
nmlist = [0 for i in range(LCamount)]

def nm(array):
    nlst = [0 for i in range(len(array))]
    std = np.std(array)
    for i in range(1, len(array)):
        nlst[i] = ((array[i] - array[i-1])**2)/((len(array)-1)*(std**2))
    n = np.sum(nlst)
    return n


for i in range(LCamount): #random Lichtkurven werden generiert
    #Produktion von künstlichen Lichtkurven
    l = random.randint(0, 5) #Helligkeit Stern
    p = random.randint(0, probability) #Wahrscheinlichkeit von 1/40

    if p == 1:
        truetruth_lst[i] = 1 #Nullen-Array an x-ter Stelle mit 1 ersetzt -> ML-Event
        # t0=0 #Zeitpunkt max. Helligkeit
        # umin=0.25
        # tE=25 #Zeitdauer, um Einstein-Radius zurückzulegen
        # standard_deviation = 0.2
        t = [0 for i in range(magpointamount)] #(start, end, Anz. Striche zwischen start und end) -> x-Achse
        #freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
        a = [0 for i in range(magpointamount)]
        umin = random.random()
        tE = random.randint(0.01, (1/2)*surveylength) #Zeitdauer, um Einstein-Radius zurückzulegen
        #random.uniform() gives random float between given range
        for x in range(magpointamount):
            t[x] = random.randint(-(1/2)*surveylength, (1/2)*surveylength)
        t.sort()
        for x in range(magpointamount):  #Helligkeit A abhängig von u, u abhängig t

            u = np.sqrt(umin**2 + ((t[x]-t0)/tE)**2)
            A = (u**2 + 2) / (u*np.sqrt(u**2 + 4)) + random.gauss(0, standard_deviation) #bei beiden Gauss-Rauschen machen
            M = -2.5*np.log10(A) - C
            a[x] = M
        lclist[i] = [i, a, t] 
        print("umin: ", umin, "tE: ", tE, "skew: ", skew(a), "std: ", np.std(a))
        #print("fit_umin: ", fit(th, t, a)[0][0], "fit_tE: ", fit(th, t, a)[0][1])
        plt.figure() #make coordinate system
        plt.plot(t, a,".", color = "red")#t,a = lists! -> A(t)+0.2*random -> adds random number to whole list -> for loop to handle each value separately!
        #plt.plot(t, th(t, fit(th, t, a)[0][0], fit(th, t, a)[0][1]))

    if p != 1: 
        
        t = [0 for i in range(magpointamount)] #(start, end, Anz. Striche zwischen start und end) -> x-Achse
        #freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
        a = [0 for i in range(magpointamount)]
        for x in range(magpointamount):
            t[x] = random.randint(-(1/2)*surveylength, (1/2)*surveylength)
        t.sort()
        for x in range (magpointamount):
            A = mean_mean + random.gauss(0, standard_deviation)
            M = -2.5*np.log10(A) - C
            a[x] = M
        lclist[i-1] = [i, a, t]
        plt.figure() #make coordinate system
        plt.plot(t, a,".", color = "red")#t,a = lists! -> A(t)+0.2*random -> adds random number to whole list -> for loop to handle each value separately!

for i in range(LCamount):
    skewlist[i] = skew(lclist[i][1])
    stdlist[i] = np.std(lclist[i][1])
    nmlist[i] = nm(lclist[i][1])


for i in range(LCamount):
    if skewlist[i] < mean_skew : #Minus weil sonst zu streng, lieber zu viel erkannt als eine nicht erkannt -> garantiert keine ML gehen verloren (wahrscheinlich doch unnötig nach Überprüfung, doch mal beibehalten)
        filterlst[i] = 1 #bei jeweiligem Index von LC steht Anzahl bestandener Filter
for i in range(LCamount):
    if stdlist[i] > mean_std: 
        filterlst[i] = filterlst[i] + 1
for i in range(LCamount):
    if nmlist[i] < np.mean(nmlist):
        filterlst[i] = filterlst[i] + 1
    #Standardabweichung
#if np.count_nonzero(truetruth_lst == 0) != LCamount: #if no ML-Event -> false trues
for i in range(LCamount): 
    if filterlst[i] == filternumber: #hat jeweiliger Index i alle Tests bestanden?
        truthlst[i] = 1 # Lichtkurve an gewisser Stelle alle Filter bestanden -> gleiche Stelle in truthlst mit 1 markieren

def filteredlc(): #damit man von anderen files darauf zugreifen kann
    filteredlc = []
    for i in range(LCamount):
        if truthlst[i] == 1: 
            filteredlc.append([lclist[i]])
    return filteredlc

lost = []
trap = []
found = []
for i in range(LCamount):
    if truthlst[i] != truetruth_lst[i]:
        if truthlst[i] - truetruth_lst[i] < 0: #wenn ML verloren ging
            lost.append(1)
            
        else:
            trap.append(1) #angebliches ML
    elif truthlst[i] + truetruth_lst[i] == 2:
        found.append(1) 

#print("TEST (-> Fehlversuch falls 0): ", np.count_nonzero(truthlst == 1))#?????
if np.count_nonzero(truthlst == 1) != 0: #wenn kein sog "Fehlversuch"
    print("verlorene ML: ", len(lost))
    print("scheinbare ML: ", len(trap))
    print("gefundene ML: ", len(found))
    print(truetruth_lst)
    print(truthlst)

else:
    print("Noch nicht verstandener scheinbarer Fehlversuch. Nochmal ausführen bis es klappt.")