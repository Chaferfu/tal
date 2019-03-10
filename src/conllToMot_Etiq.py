import sys
import re

#Transforme .conll en un texte format Mot_postag
lineNb = 1

with open(sys.argv[2], "w") as out:

    with open(sys.argv[1]) as file:
        for line in file:
            if line != '\n':
                info = line.strip().split("\t") #on recupere le mot et le tag
                w, tag = info[1], info[3]
                # if lineNb == 89: print(w) #pour debug
                w = re.sub('\s+', 'Espace', w)
                # if lineNb == 89:
                #     print(w)
                out.write(w + "_" + tag + " ") #on l'ecrit dans le fichier destination
            else:
                out.write("\n")
            lineNb += 1

