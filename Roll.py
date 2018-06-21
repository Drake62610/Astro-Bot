from random import *

nb_de=nb_face=0
while(nb_de<=0):
    nb_de = int(input("Entrez le nombre de dés : "))
while(nb_face<=0):
    nb_face = int(input("Entrez le nombre de faces: "))

resultat=[]

def lancer(nb_de,nb_face):
    for i in range(0,nb_de):
        resultat.append(randint(1,nb_face))
    return resultat


print(lancer(nb_de,nb_face))
