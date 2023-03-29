import matplotlib.pyplot as plt
import numpy as np

pH=np.linspace(0,14,101)			#Tableau des abscisses (pH)
Ka1=10**-2.0					    #Valeurs des pKa
Ka2=10**-2.7
Ka3=10**-6.2
Ka4=10**-10.3								
AH4=[]                              #Définition des listes des pourcentages des espèces acidobasiques
AH3=[]						
AH2=[]
AH=[]
A=[]

for i in range(0,101):				#Génération des listes des pourcentages en espèces acidobasiques
    h=10**-pH[i]        				#Valeur de la concentration [H3O+] pour un pH[i] donné
    M=np.array(([Ka1,-h,0,0,0],[0,Ka2,-h,0,0],[0,0,Ka3,-h,0],[0,0,0,Ka4,-h],[1,1,1,1,1]))	#Définiton de la matrice M pour un pH[i] donné
    C=np.array([0,0,0,0,100])			#Définition de la matrice C (peut être sortie de la boucle)
    X=np.linalg.solve(M,C)				#Recherche de la composition du système (en %)
    AH4.append(X[0]) 				    #Remplissage progressif des listes de composition	
    AH3.append(X[1])
    AH2.append(X[2])
    AH.append(X[3])
    A.append(X[4])

plt.figure()					    #Création d’une nouvelle figure (évite les superpositions)
plt.plot(pH,AH4,label='H4Y')
plt.plot(pH,AH3,label='H3Y-')
plt.plot(pH,AH2,label='H2Y2-')
plt.plot(pH,AH,label='HY3-')
plt.plot(pH,A,label='Y4-')
plt.axis([0,14,0,100]) 				#Définition du repère pH=[0;14] & %=[0;100]
plt.grid()					        #Ajout d'une grille
plt.title('Diagramme de distribution (H4Y)')	#Titre du graphique
plt.xlabel('pH')					#Libeller de l'axe des abscisses
plt.ylabel('Proportions (%)')		#Libeller de l'axe des ordonnées
plt.legend()					    #Ajout de la légende
plt.show()