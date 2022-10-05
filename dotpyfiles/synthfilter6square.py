import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, skew, kurtosis
from scipy.optimize import curve_fit as fit
import random

"""
Der Datensatz generiert Lichtkurvenliste der Anzahl LCamount. Jede Liste enthält 7 Einträge:
Index 0: id
1: Liste der Zeitpunkte
2: Liste der Magnitudenwerte
3: Falls ML-Event: umin-Wert
   sonst: None
4: Falls ML-Event: tE-Wert (Dauer des ML-Events)
   sonst: None
5: Skewness
6: Neumann-Wert
"""

# VALUES
probability = 1 # pro x (Probability) LC hat es ca. i ML-Event
magpointamount_min = 30 # Mindestanzahl Messungen
t0 = 0 # Zeitpunkt max. Helligkeit
surveylength = 500 # wie lange gesamte Messung dauerte = maximale Eventdauer
mean_skew = -0.22994225279524635  #Mittelwert von 2 fields 
mean_std = 0.15856555  # Mittelwert von 2 fields 
mean_mag = 20.421268  # Mittelwert von 2 fields
mean_luminosity = 10**(mean_mag/(-2.5)) # convert magnitude-mean to luminosity-value for multiplication by amplification factor 
mean_neumann = 1.6 # circa
C = 0 # parameter for magnitude-calculation
LCamount = 2000 # x LCs will be generated -> here: 2000 because 10h time to calculate overnight
foundlostrelations_list = []
skew_neumann_combinations = []

# FUNCTIONS
def theo(t, umin, tE): #theoretische ML-Funktion, returns mag
    t_0 = 0
    u = np.sqrt(umin**2 + ((t-t_0)/tE)**2)
    A = mean_luminosity*((u**2 + 2) / (u*np.sqrt(u**2 + 4))) 
    M = -2.5*np.log10(A) 
    return M

def neumann(array):
    neumann_lst = np.zeros(len(array))
    std = np.std(array)
    for i in range(1, len(array)):
        neumann_lst[i] = ((array[i] - array[i-1])**2)/((len(array)-1)*(std**2))
    n = np.sum(neumann_lst)
    return n

for max_skew in [x*0.1 for x in range(-20, 11)]: # range()-Funktion lässt keine float-steps zu
    for max_neumann in [x*0.1 for x in range(5, 21)]:
        #Lists 
        lightc_lst = [0 for i in range(LCamount)] # stellt synthetischen Datensatz dar -> pro LC: Liste wie [Index (-> Object-ID), Magnitudenwerte, Zeitpunkte]
        detect_lst_binary = np.zeros(LCamount) # Array gefilterter ML-Events, np.zeros(x) macht Liste mit x Nullen
        truetruth_lst_binary = np.zeros(LCamount) # Array mit tatsächlichen ML-Events -> muss Liste sein, da np.array keine arrays speichern kann aber kein Problem, da bei ZTF kein lclist erzeugt werden muss
        lightc_lst_filtered = [] # Index (wie object ID) wird in Liste eingefügt -> am Schluss gezählt, ob alle Kriterien erfüllt
        umin_lost = []
        tE_lost = []
        umin_found = []
        tE_found = []
        lost = 0
        trap = 0
        found = 0

        # SYNTHETIC LC GENERATOR + FILTERING -> Produktion künstlicher LC -> random ML-Events oder nicht 
        for i in range(LCamount):   
            ML_yesorno = random.randint(0, probability) #Wahrscheinlichkeit von 1/40
            magpointamount = random.randint(magpointamount_min, 100)
            if ML_yesorno == 1: #falls Microlensing-Event
                t = np.zeros(magpointamount) # (start, end, Anz. Striche zwischen start und end) -> x-Achse
                # freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
                mag = np.zeros(magpointamount)
                umin = random.random()
                tE = random.randint(1, surveylength) # Zeitdauer, um Einstein-Radius zurückzulegen
                for x in range(magpointamount):
                    t[x] = random.randint(-(1/2)*surveylength, (1/2)*surveylength)
                np.ndarray.sort(t)
                for x in range(magpointamount):  # Helligkeit A abhängig von u, u abhängig t
                    M = theo(t[x], umin, tE)  + random.gauss(0, mean_std) # bei beiden Gauss-Rauschen machen
                    mag[x] = M
                    lc_skew_value = skew(mag)
                    lc_neumann_value = neumann(mag)

                lightc_lst[i] = np.array([i, t, mag, umin, tE, lc_skew_value, lc_neumann_value], dtype = object)
                if (lc_skew_value < max_skew) and (lc_neumann_value < max_neumann):
                    found += 1
                else:
                    lost += 1

                # plt.figure() #make coordinate system
                # plt.plot(t, mag,".", color = "red")#t,mag = lists! -> A(t)+0.2*random -> adds random number to whole list -> for loop to handle each value separately!

            else: 
                
                t = np.zeros(magpointamount) # (start, end, Anz. Striche zwischen start und end) -> x-Achse
                # freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
                mag = np.zeros(magpointamount)
                for x in range(magpointamount):
                    t[x] = random.randint(-(1/2)*surveylength, (1/2)*surveylength)
                np.ndarray.sort(t)
                for x in range(magpointamount):
                    M = mean_mag + random.gauss(0, mean_std)
                    mag[x] = M
                    lc_skew_value = skew(mag)
                    lc_neumann_value = neumann(mag)
                
                lightc_lst[i] = np.array([i, t, mag, None, None, lc_skew_value, lc_neumann_value], dtype = object)
                if (lc_skew_value < max_skew) and (lc_neumann_value < max_neumann):
                    trap += 1

        foundlostrelations_list.append(found/((lost+1)*(trap+1))) # -> the bigger this value, the better the filter, lost/trap+1 because otherwise /zero
        skew_neumann_combinations.append([max_skew, max_neumann])
                
                # plt.figure() # make coordinate system
                # plt.plot(t, mag,".", color = "red")#t,a = lists! -> A(t)+0.2*random -> adds random number to whole list -> for loop to handle each value separately!


        # umin-tE-Diagramm:
        # plt.figure()
        # plt.plot(tE_lost, umin_lost, ".", color = "red")
        # plt.plot(tE_found, umin_found, ".", color = "green")
        # plt.xlabel("tE")
        # plt.ylabel("umin")
        # plt.title("max skew:" + str(max_skew) + "max neumann: " + str(max_neumann))
        # plt.show()
        #plt.savefig("umin_tE_plt.jpg")

            # if np.count_nonzero(detect_lst_binary == 1) != 0: #wenn kein sog "Fehlversuch"
            #     print("verlorene ML: ", lost)
            #     print("scheinbare ML: ", trap)
            #     print("gefundene ML: ", found)
            #     print("skew ", max_skew, "neumann: ", max_neumann,"the bigger the better the filter: ", found/((lost + 1)*(trap+1))) # -> the bigger this value, the better the filter, trap+1 because otherwise /zero
            #     # print(truetruth_lst_binary)
            #     # print(detect_lst_binary)
        # else:
        #         print("Noch nicht vers8j8j888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888tandener scheinbarer Fehlversuch. Nochmal ausführen bis es klappt.")
print("maximum relation: ", max(foundlostrelations_list))
print(skew_neumann_combinations[foundlostrelations_list.index(max(foundlostrelations_list))])
