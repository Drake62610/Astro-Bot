from random import *

resultat=[]


input = (input("Entrez les paramètres des dés, par exemple 1d6 : "))
#traintement de l'input
nb_de = int(input.split('d')[0])
nb_face = int(input.split('d')[1])


def lancer(nb_de,nb_face):
    for i in range(0,nb_de):
        resultat.append(randint(1,nb_face))
    return resultat


print("Les dés sont : ",lancer(nb_de,nb_face))

print("La somme obtenue est : ",sum(resultat))
