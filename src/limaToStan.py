import sys 
import re

#passe un fichier .conll au format de stanford pour les entites nommées mot/ENTITE, doit etre lance depuis un repertoire contenant tableCorrespondance.txt (racine ou src)

correspondance = {}
lineNb = 1 #used in debug

with open("tableCorrespondance.txt") as f:
    for line in f:
        w = line.split()
        correspondance[w[0]] = w[1]

# print(correspondance) #  {'Organization.ORGANIZATION': 'ORGANIZATION', 'Location.LOCATION': 'LOCATION', 'Person.PERSON': 'PERSON', '_': 'O'}

with open(sys.argv[2], "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            if line != '\n':
                info = line.strip().split("\t")
                w, se = info[1], info[5]
                # if lineNb == 89: print(w)
                w = re.sub('\s+', 'Espace', w)
                # if lineNb == 89:
                #     print(w)
                out.write(w + "/" + correspondance[se] + " ")
            else:
                out.write("\n")
            lineNb += 1

