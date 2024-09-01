##importation des modules
import serial
import serial.tools.list_ports # pour la communication avec le port série
import matplotlib.pyplot as plt  # pour le tracé de graphe
from matplotlib import animation # pour la figure animée
# import time # gestion du temps
import numpy as np # numpy pour l'importation des donnees en format txt
from scipy.optimize import curve_fit
from scipy.integrate import simps
from scipy.signal import kaiser

liste_a = [] # liste pour stocker les valeurs de distance
liste_t_mesure =[]
liste_t = []
t_acquisition = 5.0 # en s
amax =2 # en g
amin= -2 # en g

# Fonction pour la récupération des données série venant de la carte Arduino
def recup_port_Arduino() :
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino' in p.description :
            mData = serial.Serial(p.device,9600)
    print(mData.is_open) # Affiche et vérifie que le port est ouvert
    print(mData.name) # Affiche le nom du port
    return mData


Data =recup_port_Arduino() #récupération des données

temps=0
# Data.readline()
# Data.readline()
# Data.readline()

while temps <= t_acquisition:
    line1 = Data.readline()
    # on retire les caractères d'espacement en début et fin de chaîne
    listeDonnees = line1.strip()
    # on sépare les informations reçues séparées par les espaces et on stocke ces informations dans une liste pour chacune de lignes
    listeDonnees = line1.split()


    if len(listeDonnees) == 2 : # parfois des lignes de données vides peuvent être envoyées, il faut les "écarter"
        accel = (float(listeDonnees[1].decode()))/16834 # l'acceleration selon z correspond à la 5e colonne de listeDonnees
        temps = (float(listeDonnees[0].decode()))/1000.0 # le temps correspond à la 2e colonne de listeDonnees
        liste_t_mesure.append(temps)
        if liste_t_mesure[0]< 1 : # pour éventuellement éliminer les premières valeurs fausses de temps (défaut d'Arduino)
            liste_a.append(accel)
            liste_t.append(temps)
            print("temps \t\t | \t accélération") # affichage de la valeur du temps en partant de 0
            print("%5.3f"%(temps), " s \t | \t %f"%(accel), "g") # affichage de la valeur du temps en partant de 0
        else :
            del liste_t_mesure[0]

Data.close()


#Ecriture dans un fichier txt
lines=['t\ta\n'] #première ligne du fichier txt
for i in range (len (liste_a)):
    line = str(liste_t[i]) +'\t'+ str(liste_a[i])+'\n'
    lines.append(line)

fichier = open('data_accelerometre.txt', 'w').writelines(lines) #création d'un nouveau fichier texte



t = np.array(liste_t)
acc = np.array(liste_a)

def freqfinder(sig, fe):
    n = len(sig) # longueur du signal
    k = np.arange(n)
    T = n/fe
    frq = k/T # vecteur des fréquences
    frq = frq[:len(frq)//2] # on se place sur f in 0:fe/2
    w = kaiser(n,6)
    Y = np.fft.fft(sig*w)/(n/2) # TF directe et normalisation
    Y = Y[:len(frq)]
    mod = abs(Y)
    maxPos = np.argmax(mod)
    FrqMax = frq[maxPos]
    #♠Amplitude = np.max(mod)
    n_round = round(len(frq)/10)
     #calculate energy like this
    Amplitude_energy = sum(mod[maxPos-n_round:maxPos+n_round]**2) #théorème de Parseval sur l'énergie
    Amplitude = np.sqrt(Amplitude_energy*2) # en supposant que c'est une sinusoïde
    return frq, mod, FrqMax, Amplitude


frq, mod, maxFrq, Amplitude = freqfinder(acc, (len(t)-1)/(t[len(t)-1]-t[1]))

texte2 = 'f = ' +str(round(float(maxFrq),4))+ 'Hz et amplitude = ' +str(round(float(Amplitude),3)) +'m.s-2'

#afficher points avec croix rouges.
plt.subplot(211)
plt.plot(t, acc, c = 'red')
plt.xlabel("t en s")
plt.ylabel("a en g")
#plt.legend()   # pour afficher les légendes (label)

plt.subplot(212)
plt.scatter(frq, mod, label = texte2)
plt.xlabel("f en Hz")
plt.ylabel("a en g")
plt.legend()   # pour afficher les légendes (label)

plt.show()

