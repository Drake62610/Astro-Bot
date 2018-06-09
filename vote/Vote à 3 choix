vote = [0,0,0] #Liste des choix
resultat = [0,0,0] #Liste pour compter les votes

nb_votants = int(input("Entrez le nombre de votants : "))


def notes(vote): #fonction de vote avec 3 choix (3,2 et 1 pts à attribuer)

    print("Vous ne pouvez accorder que 3, 2 et 1 points")

    while vote[0]>3 or vote[0]<1: #la note doit être 3,2 ou 1
        vote[0] = int(input("Entrez le nombre de point pour le choix 1 : "))

        if vote[0] == 3:
            while (vote[1]>2 or vote[1] < 1):
                vote[1] = int(input("Entrez le nombre de point pour le choix 2 : "))

            if vote[1] == 2:
                while (vote[2] != 1 or vote[2] == 0):
                    vote[2] = int(input("Entrez le nombre de point pour le choix 3 : "))
            if vote[1] == 1:
                while (vote[2] != 2 or vote[2] == 0):
                    vote[2] = int(input("Entrez le nombre de point pour le choix 3 : "))

        if vote[0] == 2:
            while (vote[1] > 3 or vote[1] < 1 or vote[1] == 2):
                vote[1] = int(input("Entrez le nombre de point pour le choix 2 : "))
            if vote[1] == 3:
                while (vote[2] != 1 or vote[2] == 0):
                    vote[2] = int(input("Entrez le nombre de point pour le choix 3 : "))
            if vote[1] == 1:
                while (vote[2] != 3 or vote[2] == 0):
                    vote[2] = int(input("Entrez le nombre de point pour le choix 3 : "))


        if vote[0] == 1:
            while vote[1] > 3 or vote[1] < 1 or vote[1] == 1:
                vote[1] = int(input("Entrez le nombre de point pour le choix 2 : "))
            if vote[1] == 2:
                while (vote[2] != 3 or vote[2]==0):
                        vote[2] = int(input("Entrez le nombre de point pour le choix 3 : "))
            if vote[1] == 3:
                while (vote[2] != 2 or vote[2]==0):
                        vote[2] = int(input("Entrez le nombre de point pour le choix 3 : "))

a=0
while a < nb_votants:
    notes(vote)

    resultat[0] = vote[0]+resultat[0] #compte les resultats en additionnant les listes de chaque participant avec les 3 choix
    resultat[1] = vote[1]+resultat[1]
    resultat[2] = vote[2]+resultat[2]
    print("\n")
    a = a+1 #incrémente l'indice de boucle de 1
    vote = [0, 0, 0] #reboot la valeur de la liste pour un nouveau votant


for point in enumerate(resultat): #annonce les résultats
    print(point)
