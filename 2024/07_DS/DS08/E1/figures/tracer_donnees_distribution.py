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
plt.subplots_adjust(bottom=0.18, right=0.98, top=0.85,left=0.2)

f=open("donnees_titrage.csv")
L=[]
f.readline()
for line in f :
    l=line.split(";")
    x=list(map(float,l))
    L.append(x)

T=np.array(L)   

f.close()

plt.plot(T[:,1],T[:,2],'o',ms=2,label="Courbe 1")
plt.plot(T[:,1],T[:,3],'x',ms=2,label="Courbe 2")
plt.plot(T[:,1],T[:,4],"s",ms=2,label="Courbe 3")
plt.ylabel('$x$',fontsize=10)
plt.xlabel('pH',fontsize=10)
plt.xticks(np.arange(0,14.1,2),fontsize=10)
plt.yticks(np.arange(0,1.1,0.2),fontsize=10)
plt.grid()
plt.legend(fontsize=6)
plt.title("Diagramme de distribution",fontsize=10)
plt.savefig("./graphe_distribution.pdf", bbox_inches="tight")
# plt.show()
