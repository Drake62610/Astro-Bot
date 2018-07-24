from random import *

resultat=[]

input = (input("Entrez les paramètres des dés, par exemple 1d6 : ")) #DEMANDE la commande
#TRAITEMENT de l'input
nb_de = int(input.split('d')[0])
nb_face = int(input.split('d')[1])

def lancer(nb_de,nb_face): #FONCTION qui liste les dés
    for i in range(0,nb_de):
        resultat.append(randint(1,nb_face))
    return resultat #RECUPERE la liste


print("Les dés sont : ",lancer(nb_de,nb_face)) #DONNE la liste

print("La somme obtenue est : ",sum(resultat)) #DONNE la somme de la liste