from random import *

resultat=[]

nb_de = (input("Entrez le nombre de dés : "))

try:
    nb_de = int(nb_de)
except:
    print("Ce n'est pas une nombre positive")

nb_face = (input("Entrez le nombre de faces: "))

try:
    nb_face = int(nb_face)
except:
    print("Ce n'est pas un nombre positive")



def lancer(nb_de,nb_face):
    for i in range(0,nb_de):
        resultat.append(randint(1,nb_face))
    return resultat


print("Les dés sont : ",lancer(nb_de,nb_face))

print("La somme obtenue est : ",sum(resultat))
