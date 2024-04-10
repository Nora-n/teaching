import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
def cm2inch(value):
    return value/2.54

fig = plt.figure(figsize=(cm2inch(8),cm2inch(7)))

plt.subplots_adjust(hspace=0.3)
plt.subplots_adjust(bottom=0.18, right=0.98, top=0.98,left=0.2)

f=open("donnees_titrage.csv")
L=[]
f.readline()
for line in f :
    l=line.split(";")
    x=list(map(float,l))
    L.append(x)

T=np.array(L)   

f.close()

plt.plot(T[:,0],T[:,1])
plt.ylabel('pH',fontsize=10)
plt.xlabel('$V$(mL)',fontsize=10)
plt.xticks(np.arange(0,31,5),fontsize=10)
plt.yticks(np.arange(0,14,2),fontsize=10)
plt.grid()
plt.title("Suivi pH-métrique",fontsize=10)
plt.savefig("./graphe_pH.pdf", bbox_inches="tight")
# plt.show()
