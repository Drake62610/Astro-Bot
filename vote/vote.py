nb_votants = int(input("Entrez le nombre de votants : "))
nb_choix = int(input("Entrez le nombre de choix : "))

note = []
vote = []


def votants(nb_choix,vote):
    j = 0
    for i in range(0,nb_choix):
        j += 1

        vote.append(int(input("Entrez le nombre de point pour le choix {} :".format(j))))

    return vote


i = 0
for i in range(0,nb_votants):
    note.append(votants(nb_choix,vote)) #A envoyer à un joueur à la fois.
    print("\n")
    vote = []

for points in note:
  print(points)
