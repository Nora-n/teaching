import   numpy   as  np
N  =  100000  #  nombre  de  tirages
R  =  []  # initialisation   liste   vide
U  =  [1.4   ,  1.6]  # intervalle  de  la  tension
I  =  [0.121 ,   0.123]  # intervalle  de  l’intensite
for  i  in  range (N):
    Utir  =  np. random . uniform (U[0] ,  U [1])
    Itir  =  np. random . uniform (I[0] ,  I [1])
    R. append ( Utir / Itir )
#  détermination   du  résultat  de  mesurage  ( arrondi )
Rmes  =  round (sum(R)/N ,4)
Rinc  =  round (np. std (R) ,4)
# affichage
str_aff  =  'R  =  '  +  str( Rmes )  +  '  +/-  '  +  str( Rinc )  +  '  Ohm '
print ( str_aff )
