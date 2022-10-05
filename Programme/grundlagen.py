print("Grundlagen von Python\n")

#Kommentare
print("Einzeilige Kommentare weren als #Bla bla eingegeben, mehrzeilige Kommentare")
print("durch Abgrenzung mit drei Anführungszeichen '''Bla bla ... bla'''\n")

#Typen und Typenkonversionen
print("Eine Variabel a kriegt automatisch ihren Typ adaptiert.")
print("Die Eingabe a = 2.5 weist a den Typ float zu.")
a=2.5
print("OUT: a =", a, "mit Typ", type(a),"\n")
print("Ebenso funktioniert das mit dem Typ bool und integer.")
b=True
c=2
print("OUT: b =", b, "mit Typ", type(b))
print("OUT: c =", c, "mit Typ", type(c),"\n")
print("Mit str(.) kann man Zahlen in Strings umwandeln. Strings lassen sich addieren.")
s=str(c)+'llinge'
print("OUT: s = str(c)+'llinge' ergibt", s, "mit Typ", type(s),"\n")

#Typenkonversion geht automatisch
print("Die Variabeltypen werden spontan angepasst, wie das folgende Beispiel zeigt:")
k=2
print("OUT: k =", k, "mit Typ", type(k))
k*=7.2
print("OUT: k *= 7.2 =", k, "mit Typ", type(k))
print("Typenkonversionen können mit int(), float(), complex() auch erzwungen werden.\n")

#Mathematische Grundoperationen
print("Die gängigen matehmatischen Operationen sind klar, Typen werden angepasst.")
d=1+3.3
print("OUT: d = 1 + 3.3 =", d, "mit Typ", type(d))
e=2.0*4
print("OUT: e = 2.0 * 4 =", e, "mit Typ", type(e))
f=6.0/3   
print("OUT: f = 6.0 / 3 =", f, "mit Typ", type(f))
print("Achtung: Bei Divisionnen resultiert immer der Typ float.")
g=6/3
print("OUT: g = 6 / 3 =", g, "mit Typ", type(g),"\n")
print("Wie immer muss man bei den ganzzahligen Divisonen genauer hinschauen.")
h=7//3
print("OUT: h = 7 // 3 =", h, "mit Typ", type(h))
i=7%3   
print("OUT: i = 7 % 3 =", i, "mit Typ", type(i),"\n")
print("Potenzieren erfolgt mit ** statt wie gewohnt mit ^.")
l=2**3    
print("OUT: l = 2 ** 3 =", l, "mit Typ", type(l),"\n")
print("Schliesslich existieren wie in C die Kombinationen *=, +=, -=, /=, //= und %=.\n")

#Einfache Schleifen und Verzweigungen
print("Einfache Schleifen funktionieren wie folgt:")
print("for-Schleife: von und mit 3 bis und ohne 9 im Abstand 2...")
for ele in range(3,9,2):
    print(ele)
print("\nfor-Schleifen können auch mit Listen gesteuert werden (siehe später: Arrays)")
names=["Peter","Hans","Anna","Lucie"]
for s in names:
    print(s)
    
print("\nwhile-Schleife: solange n nicht negativ immer zwei abzählen ausgehend von 4...")
n=4
while(n>=0):
    print(n)
    n-=2
print("\noder falls n=gerade dann n/2, sonst 3*n+1...")
n=4
if(n%2==0):
    n//=2
else:
    n=3*n+1
print("OUT: n = 4 liefert n =",n)
n=5
if(n%2==0):
    n//=2
else:
    n=3*n+1
print("OUT: n = 5 liefert n =",n)
print("Interessant ist die Möglichkeit der Mehrfachentschedung mit if - elif - elif - elif - else.")
print("Der Ausstieg aus Schleifen kann mit break gemacht werden:")
x=0
while 1:
    print(x)
    x+=1
    if x>5:
        break
print("\nDie Vergleichsoperatoren sind ==, !=, >=, <=, > und <.")
print("Die logischen Operatoren sind not x, x or y, x and y\n")

#Einfache Funktionen
print("Einfache Programme hier am Beispiel der Berechnung des Drucks")
print("für gegebene Höhe h über Meer in Standardatmosphäre,")
print("Masseinheit hPa. Gültig für 0 < h < 11‘000m")

#Constants
p_std = 1013.25     # Standarddruck auf Meereshöhe
c1 = 0.0065/288.15
c2 = 5.255

#eigentliches Programm
def pressure(height):
    result = (1.0-c1*height)**c2
    return p_std*result

print("\nDer Funktionsaufruf ergibt das korrekte Resultat")
print("OUT: pressure(500) liefert p =",pressure(500),"hPa.\n")
print("eine beliebige Anzahl Argumente wird mit func(*arg) programmiert.\n")
print("Funktionen haben ihren eigenen namespace. Mit 'global' gelten Variabeln überall.\n")

#Bibliotheken
print("Die wichtigsten Bibliotheken sind numpy, scipy und pyplot, folgendermassen einzubinden:")
print("import numpy as np")
print("from matplotlib import pyplot as plt")
print("import scipy\n")
print("Man kann aber von jedem File darin enthaltene Funktionen importieren, entweder via")
print("from filename import functionname")
print("oder global alle darin enthaltenen Files mit")
print("from filename import *")
print("Die FUnktionen müssen immer auf den namespace des importierten Pakets bezogen werden, also paket.func().\n")

#Vektoren, Matrizen und allg. Felder mit numpy
import numpy as np
print("Ein Vektor (1,2,3,4) wird folgendermassen generiert: vec=np.array([1,2,3,4])")
vec=np.array([1,2,3,4])
print("OUT: vec =",vec)
print("Der Zugriff erfolgt via")
print("OUT: erste Stelle: vec[0] =",vec[0])
print("OUT: letzte Stelle: vec[-1] =",vec[-1])
print("OUT: zweite und dritte Stelle (lies: Pos 1 bis 3-1): vec[1:3] =",vec[1:3])
print("Der Datentyp eines Arrays kann erzwungen werden mit vec=np.array([1,2,3],'float').")
print("\nListen gibt es auch ausserhalb von numpy - dann ohne den array-Befehl.")
print("Der Befehl array macht eine Liste zu einem Array.")
print("Interessant ist, dass allgemeine Listen gemischt sein können wie zB s=[1,2,'a',[1,3]].")

print("\nEinige interessante Anwendungen von numpy:")
print("Vektor der Länge 3 mit Nullen initialisiert: np.zeros(3)")
vec2=np.zeros(3)
print("OUT: vec2 =",vec2)
print("\n3x4-Matrix 3 mit Nullen initialisiert: np.zeros((3,4))")
mat=np.zeros((3,4))
print("OUT: mat =",mat)
print("\nVektor der Länge 10 mit Einsen initialisiert: np.ones(10)")
vec3=np.ones(10)
print("OUT: vec3 =",vec3)
print("\nVektor mit Zahlen von 1 bis keiner als 11 in Abständen 2 initialisiert: np.arange(1,11,2)") 
vec4=np.arange(1,11,2)
print("OUT: vec4 =",vec4)
print("\nVektor mit Intervall von 1 bis 2 in 5 Abschnitte unterteilt initialisiert: np.linspace(1,2,5)") 
vec5=np.linspace(1,2,5)
print("OUT: vec5 =",vec5)
print("\nDas innere Produkt zweier passender Objekte A und B läuft mit np.dot(A,B)") 
B=np.array([1,2,3,4])
A=np.ones((3,4))
C=np.dot(A,B)
print("OUT: A =",A)
print("OUT: B =",B)
print("OUT: A.B =",C)
print("\nWeitere selbsterklärende Befehle auf Vektoren sind")
print("np.mean(x), np.sum(x), np.median(x), np.max(x), np.min(x)") 
print("\nACHTUNG: Für zwei Arrays macht a=b keinen neuen Array a. Man muss a=np.copy(b) machen.")
D=A
E=np.copy(A)
D[0,0]=2
print("OUT: D=A, E=np.copy(A), D[0,0]=2 -> A[0,0] =",A[0,0],"und E[0,0] =",E[0,0])


print("\nArithmetische Operationen mit Vektoren funktionieren wo sinnvoll elementweise, das heisst z.B.")
print("OUT: np.sin(B) =",np.sin(B),"oder")
print("OUT: B+B =",B+B,"oder")
print("OUT: B*B =",B*B,"\n")

#Pseudo-Zufallszahlen in [0,1)
print("Zufallszahlen werden ebenfalls über numpy erstellt")
print("OUT: np.random.random(7) =",np.random.random(7),"\n")

#Komplexe Zahlen 
print("Komplexe Zahlen werden mit dem Befehl complex generiert, z.B. so:")
z=complex(0.5,1)
print("OUT: z=complex(0.5,1) =",z)
print("OUT: z^2 =",z*z,"\n")
print("Alternativ kann auch einfach 4+3j (NICHT 3*j!!) eingegeben werden")
z=4+3j
print("OUT: z =",z)
print("Real- und Imaginärteil kriegt man mit z.real und z.imag")
print("OUT: Re(z) =",z.real)
print("OUT: Im(z) =",z.imag)

#Mathematische Operationen
print("\nKomplexe math. Operationen wie FFT, Differentiation, Faltung etc. finden sich in scipy.")

#Plots
print("\nEin einfacher 2D-Plot aus Zufallszahlen erfolgt mit plt.plot(x,y,‘bo‘)")
x = np.random.random(100)
y = np.random.random(100)
from matplotlib import pyplot as plt
plt.plot(x,y,'bo')
print("\nMit plt.savefig('testplot.png') wird der Plot als File im selben Ordner wie der Source Code gespeichert.")
print("Mit dpi kann die Auflösung des gespeicherten (!) Bildes gesteuert werden.")
print("WICHTIG: zuerst sichern, erst dann mit plt.show() anzeigen!")
plt.savefig('testplot.png',dpi=300)
plt.show()      # Zeige den plot in neuem Fenster
print("\nWeitere wichtige Befehle zu Plots sind im Beispiel pyplot_example.py")

#Objekte löschen
print("\nMit del lassen sich Objekte oder Teile von Listen löschen:")
a=5
del a
a=[1,2,3,4,5]
del a[3:4]
print("Out: a=[1,2,3,4,5] -> del a[3:4] -> a =",a,"\n")

#Filehandling
print("Das Einlesen und Schreiben von Files geschieht zB so wie im Code gezeigt.")
print("Möglicherweise geht das noch eleganter...\n")
inp=open('datenfile.txt','r')   #Stream datenfile -> Variable inp
line=inp.readline()             #Erste Kommentarzeile wird gelesen
dt=float(inp.readline())        #zweite Zeile wird als float in dt abgelegt
i=0
xdata=[]
ydata=[]
for line in inp:                #für restliche Linien
    yvalues = line.split()      #Daten werden in 2dim yvalues abgelegt
    xdata.append(float(yvalues[0]))
    ydata.append(float(yvalues[1]))
inp.close

out=open('output.txt','w')
for step in range(0,len(xdata)):
    out.write('%g %g\n' % (xdata[step],ydata[step]))
out.close

#Bugs und Probleme
#Python ist empfindlich auf versteckte Linefeeds, Tabs, Tabs statt Leerzeichen und dergleichen.
#Kopieren des Programmcodes in TextEdit hilft manchmal, um solchen Scheiss zu entdecken. 