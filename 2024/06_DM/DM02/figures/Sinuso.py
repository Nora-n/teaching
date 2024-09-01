# -*- coding: utf-8 -*-
"""
Filtre passe-bas ordre 2
"""
#from math import sqrt 

from pylab import *

from scipy.signal import lti

# Caractéristiques du filtre
f0=2e3
xi=1/sqrt(2)

numerateur=1

denominateur = [1/f0**2,2*xi/f0,1] #passe bas d'ordre 2

filtre = lti(numerateur,denominateur)

f = arange(10,1e5,50)
f,GdB,phase=filtre.bode(f)

#Tracé du diagramme de Bode
semilogx(f,GdB)
plt.title("Réponse en gain")
plt.xlabel("Hz")
plt.ylabel("GdB")
figure()
plt.title("Réponse en phase")
plt.xlabel("Hz")
plt.ylabel("degré")
semilogx(f,phase)

#Action du filtre sur la sinusoïde
fs = 500 #fréquence du signal en Hz
a = 2 # amplitude

N=1024

Te=5e-6

t=arange(0,N*Te,Te)

entree_sin = a*sin(2*pi*fs*t)

figure()
#representation du signal d'entree
plot(t,entree_sin,label="entrée",color="gray")
ylim([-2.5,2.5])

#Obtention du spectre du signal d'entree
spectreentree=fft(entree_sin)

f=fftfreq(N,Te) #crée un vec

spectresortie=spectreentree*(filtre.freqresp(f,N)[1])

sortie_sin=ifft(spectresortie)

plot(t,sortie_sin,label="sortie",color="blue")
plt.legend()


#Action du filtre sur le signal créneau
fs = 50 #fréquence du signal en Hz
a = 2 # valeur max du créneau

N=1024

Te=1e-5

t=arange(0,N*Te,Te)

entree_creneau = [a if cos(2*pi*fs*ti)>=0 else 0 for ti in t]

figure()
#representation du signal d'entree
plot(t,entree_creneau,label="entrée",color="gray")
ylim([-0.5,2.5])

#Obtention du spectre du signal d'entree
spectreentree=fft(entree_creneau)

f=fftfreq(N,Te) #crée un vec

spectresortie=spectreentree*(filtre.freqresp(f,N)[1])

sortie=ifft(spectresortie)

plot(t,sortie,label="sortie",color="blue")
plt.legend()
plt.show()