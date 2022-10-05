import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, skew, kurtosis
from scipy.optimize import curve_fit as fit
import random

# overall values
filternumber = 2
probability = 1
t0 = 0 # Zeitpunkt max. Helligkeit
surveylength = 500 # wie lange gesamte Messung dauerte = maximale Eventdauer
standard_deviation = 0.2
mean_skew = -0.22994225279524635  #Mittelwert von 2 fields 
mean_std = 0.15856555  # Mittelwert von 2 fields 
mean_mean = 20.421268  # Mittelwert von 2 fields 
mean_neumann = 10000 # zwar viel höher als Mittelwert aller nms, aber hohe Standardabweichung ohne ML-Event lässt sich nur mit sehr überdurchschnittlich hohem nm erreichen --> ...- doch nicht?
C = 0 # parameter for magnitude-calculation
LCamount = 100

"""
Hier ist zum Dokumentieren
"""

# LISTS
lightc_lst = [0 for i in range(LCamount)] # stellt synthetischen Datensatz dar -> pro LC Liste wie [Index (-> Object-ID), Magnitudenwerte, Zeitpunkte] 
detect_lst_binary = np.zeros(LCamount) # Liste gefilterter ML-Events, np.zeros(x) macht Liste mit x Nullen
truetruth_lst_binary = np.zeros(LCamount) # Liste mit tatsächlichen ML-Events
# -> muss Liste sein, da np.array keine arrays speichern kann aber kein Problem, da bei ZTF kein lclist erzeugt werden muss
lightc_lst_filtered = [] # Index (wie object ID) wird in Liste eingefügt -> am Schluss gezählt, ob alle Kriterien erfüllt
skew_lst = np.zeros(LCamount) # Skewness-Werte alles LC
std_lst = np.zeros(LCamount) # Standardabw-Werte alles LC
neumann_lst = np.zeros(LCamount)

def neumann(array):
    neumann_lst = np.zeros(len(array))
    std = np.std(array)
    for i in range(1, len(array)):
        neumann_lst[i] = ((array[i] - array[i-1])**2)/((len(array)-1)*(std**2))
    n = np.sum(neumann_lst)
    return n


for i in range(LCamount): # random Lichtkurven werden generiert
    # Produktion von künstlichen Lichtkurven
    lc_yesorno = random.randint(0, probability) #Wahrscheinlichkeit von 1/40
    magpointamount_min = 30
    magpointamount = random.randint(30, 100)
    if lc_yesorno == 1:
        truetruth_lst_binary[i] = 1 #Nullen-Array an x-ter Stelle mit 1 ersetzt -> ML-Event
        # t0=0 #Zeitpunkt max. Helligkeit
        # umin=0.25
        # tE=25 #Zeitdauer, um Einstein-Radius zurückzulegen
        # standard_deviation = 0.2
        t = np.zeros(magpointamount) # (start, end, Anz. Striche zwischen start und end) -> x-Achse
        # freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
        mag = np.zeros(magpointamount)
        umin = random.random()
        tE = random.randint(1, surveylength) # Zeitdauer, um Einstein-Radius zurückzulegen
        # random.uniform() gives random float between given range
        for x in range(magpointamount):
            t[x] = random.randint(-(1/2)*surveylength, (1/2)*surveylength)
        np.ndarray.sort(t)
        luminosity = 10**(mean_mean/(-2.5)) # convert magnitude-mean to luminosity-value for multiplication by amplification factor 
        for x in range(magpointamount):  # Helligkeit A abhängig von u, u abhängig t
            u = np.sqrt(umin**2 + ((t[x]-t0)/tE)**2)
            A = luminosity*(u**2 + 2) / (u*np.sqrt(u**2 + 4))  # bei beiden Gauss-Rauschen machen
            M = -2.5*np.log10(A) - C + random.gauss(0, standard_deviation)
            mag[x] = M
        # plt.plot(a)

        lightc_lst[i] = np.array([i, mag, t, umin, tE], dtype = object)
        # print("umin: ", umin, "tE: ", tE, "skew: ", skew(mag), "std: ", np.std(mag))
        # print("fit_umin: ", fit(th, t, mag)[0][0], "fit_tE: ", fit(th, t, mag)[0][1])
        # plt.figure() #make coordinate system
        # plt.plot(t, mag,".", color = "red")#t,mag = lists! -> A(t)+0.2*random -> adds random number to whole list -> for loop to handle each value separately!
        # #plt.plot(t, th(t, fit(th, t, mag)[0][0], fit(th, t, mag)[0][1]))

    else: 
        
        t = np.zeros(magpointamount) # (start, end, Anz. Striche zwischen start und end) -> x-Achse
        # freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
        mag = np.zeros(magpointamount)
        for x in range(magpointamount):
            t[x] = random.randint(-(1/2)*surveylength, (1/2)*surveylength)
        np.ndarray.sort(t)
        for x in range(magpointamount):
            luminosity = 10**(mean_mean/(-2.5)) # convert magnitude-mean to luminosity-value for multiplication by amplification factor 
            M = -2.5*np.log10(luminosity) - C + random.gauss(0, standard_deviation)
            mag[x] = M
        # plt.plot(a)
        lightc_lst[i] = np.array([i, mag, t, None, None], dtype = object)
        # plt.figure() # make coordinate system
        # plt.plot(t, a,".", color = "red")#t,a = lists! -> A(t)+0.2*random -> adds random number to whole list -> for loop to handle each value separately!

for i in range(LCamount):
    skew_lst[i] = skew(lightc_lst[i][1])
    std_lst[i] = np.std(lightc_lst[i][1])
    neumann_lst[i] = neumann(lightc_lst[i][1])

# for i in range(LCamount):
#     if skewlist[i] < mean_skew : #Minus weil sonst zu streng, lieber zu viel erkannt als eine nicht erkannt -> garantiert keine ML gehen verloren (wahrscheinlich doch unnötig nach Überprüfung, doch mal beibehalten)
#         filterlst[i] = 1 #bei jeweiligem Index von LC steht Anzahl bestandener Filter
for i in range(LCamount):
    if skew_lst[i] - 0.5 < -neumann_lst[i]:
        detect_lst_binary[i] = 1
        lightc_lst_filtered.append(lightc_lst[i]) # lclist[i] = numpy-array 
    else:
        detect_lst_binary[i] = 0
    # print(truetruth_lst[i],stdlist[i],detectlst[i])

def filteredlc(): # damit man von anderen files darauf zugreifen kann
    return filtered_lst
lost = 0
trap = 0
found = 0
umin_lost = []
tE_lost = []
umin_found = []
tE_found = []
filtered_lst = []

for i in range(LCamount):
    if ((truetruth_lst_binary[i] == 1) and (detect_lst_binary[i] == 1)):
        found+=1
        umin_found.append(lightc_lst[i][3])
        tE_found.append(lightc_lst[i][4])
        filtered_lst.append(lightc_lst[i])
    if ((truetruth_lst_binary[i] == 1) and (detect_lst_binary[i] == 0)):
        lost+=1
        umin_lost.append(lightc_lst[i][3])
        tE_lost.append(lightc_lst[i][4])

    if ((truetruth_lst_binary[i] == 0) and (detect_lst_binary[i] == 1)):
        trap+=1


# umin-tE-Diagramm:
plt.figure()
plt.plot(tE_lost, umin_lost, ".", color = "red")
plt.plot(tE_found, umin_found, ".", color = "green")
plt.xlabel("tE")
plt.ylabel("umin")
plt.show()
# print("TEST (-> Fehlversuch falls 0): ", np.count_nonzero(truthlst == 1))#?????
if np.count_nonzero(detect_lst_binary == 1) != 0: #wenn kein sog "Fehlversuch"
    print("verlorene ML: ", lost)
    print("scheinbare ML: ", trap)
    print("gefundene ML: ", found)
    # print(truetruth_lst)
    # print(detectlst)
else:
    print("Noch nicht verstandener scheinbarer Fehlversuch. Nochmal ausführen bis es klappt.")