from random import *

def lancer(input): #FONCTION qui liste les dés
    resultat=[]
    nb_de = int(input.split('d')[0])
    nb_face = int(input.split('d')[1])

    for i in range(0,nb_de):
        resultat.append(randint(1,nb_face))
    return resultat #RECUPERE la liste
