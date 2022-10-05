import numpy as np
from matplotlib import pyplot as plt
import random 

length = 10
truth_lst = np.zeros(length) #np.zeros(x) macht Liste mit x Nullen
frequency = 7 #1 Messung in x Tagen
probability = 5

def f():
    import numpy as np
    from matplotlib import pyplot as plt
    import random 

    length = 10
    truth_lst = np.zeros(length) #np.zeros(x) macht Liste mit x Nullen
    frequency = 7 #1 Messung in x Tagen
    probability = 5
    for x in range(0, length): #40 random Lichtkurven werden generiert
        #Produktion von künstlichen Lichtkurven
        l = random #Helligkeit Stern
        p = random.randint(0, probability) #Wahrscheinlichkeit von 1/40

        if p == 1:
            truth_lst[x] = 1 #Nullen-Array an x-ter Stelle mit 1 ersetzt -> ML-Event
            t0 = 0 #Zeitpunkt max. Helligkeit
            umin = 0.25
            standard_deviation = 0.5
            tE = 25 #Zeitdauer, um Einstein-Radius zurückzulegen

            t = np.linspace(-50, 50, 100) #(start, end, Anz. Striche zwischen start und end) -> x-Achse
            #freie Parameter hängen von t ab -> verändern sich mit der Zeit -> Körper bewegen sich
            a = []
        
            for x in t:  #Helligkeit A abhängig von u, u abhängig t
                y = random.randint(0, frequency) #Messung ca. einmal in 30 Tagen
                if y == 1: 
                    u = np.sqrt(umin**2 + ((x-t0)/tE)**2)
                    A = (u**2 + 2) / (u*np.sqrt(u**2 + 4)) + random.gauss(0, standard_deviation) #bei beiden Gauss-Rauschen machen
                    a.append(A)
                else: 
                    a.append(None)

            plt.figure()
            plt.plot(t, a,".", color = "red")
            return a


        if p != 1: 
            mean = 4#randomize -> bei ZTF nachschauen -> uniform()
            standard_deviation = 0.5
            
            t = np.linspace(-50, 50, 100) #(start, end, Anz. Striche zwischen start und end) -> x-Achse
            
            a = []
            
            for i in t:
                y = random.randint(0, frequency)
                if y == 1:
                    A = mean + random.gauss(0, standard_deviation)
                    a.append(A)
                else:
                    a.append(None)
                #müssen nicht geplottet werden, nur Zahlen notwendig

            return a
    def t():
        return truth_lst
    


        #Speichern, welche Kurve ML ist
        #Filterung der Lichtkurven
        #Ausgangslage: a, t...
        #wenn Filter überlebt neue Routine, die nur über 1er geht oder separater Loop -> Theorie vergleichen 
